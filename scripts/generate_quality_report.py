"""
Generate data quality report from pytest results
and update table documentation
"""
import subprocess
import json
import yaml
from pathlib import Path
from datetime import datetime
import re

def run_tests():
    """Run pytest and capture results"""
    result = subprocess.run(
        ['pytest', 'tests/data_quality/', '--json-report', '--json-report-file=tests/reports/results.json', '-v'],
        capture_output=True,
        text=True
    )
    return result

def load_test_definitions():
    """Load test definitions"""
    yaml_path = Path("tests/data_quality/data_test_definition.yaml")
    with open(yaml_path) as f:
        return yaml.safe_load(f)

def generate_markdown_report(results, definitions):
    """Generate markdown report from test results"""
    
    # Parse results (adjust based on your pytest-json-report format)
    # This is simplified - adjust to your actual JSON structure
    
    md = f"# Data Quality Report\n\n"
    md += f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # Summary statistics
    total_tests = len(results.get('tests', []))
    passed = sum(1 for t in results.get('tests', []) if t.get('outcome') == 'passed')
    failed = total_tests - passed
    
    md += "## Summary\n\n"
    md += f"- **Total Tests**: {total_tests}\n"
    md += f"- **Passed**: {passed} ✓\n"
    md += f"- **Failed**: {failed} ✗\n"
    md += f"- **Pass Rate**: {(passed/total_tests*100):.1f}%\n\n"
    
    # Group by category
    categories = {}
    for category_name, tests in definitions.items():
        categories[category_name] = {
            'total': len(tests),
            'passed': 0,
            'failed': 0,
            'tests': []
        }
    
    # Categorize test results
    for test_result in results.get('tests', []):
        test_id = extract_test_id(test_result.get('nodeid', ''))
        
        # Find test definition
        test_def = find_test_definition(test_id, definitions)
        if test_def:
            category = test_def['category']
            if test_result.get('outcome') == 'passed':
                categories[category]['passed'] += 1
            else:
                categories[category]['failed'] += 1
            
            categories[category]['tests'].append({
                'definition': test_def,
                'result': test_result
            })
    
    # Write category sections
    for category_name, category_data in categories.items():
        md += f"## {category_name.replace('_', ' ').title()}\n\n"
        md += f"**Pass Rate**: {category_data['passed']}/{category_data['total']}\n\n"
        
        # Failed tests first
        failed_tests = [t for t in category_data['tests'] if t['result'].get('outcome') != 'passed']
        if failed_tests:
            md += "### ❌ Failed Tests\n\n"
            for test in failed_tests:
                test_def = test['definition']
                md += f"#### {test_def['id']}: {test_def['name']}\n\n"
                md += f"**Severity**: {test_def['severity'].upper()}\n\n"
                md += f"**Description**: {test_def['description']}\n\n"
                md += f"**Affected Tables**: {', '.join([f'`{t}`' for t in test_def['tables']])}\n\n"
                md += f"**Rationale**: {test_def['rationale']}\n\n"
                md += f"**Remediation**:\n{test_def['remediation']}\n\n"
                md += "---\n\n"
        
        # Passed tests summary
        passed_tests = [t for t in category_data['tests'] if t['result'].get('outcome') == 'passed']
        if passed_tests:
            md += "### ✅ Passed Tests\n\n"
            for test in passed_tests:
                test_def = test['definition']
                md += f"- **{test_def['id']}**: {test_def['name']}\n"
            md += "\n"
    
    md += "\n"
    
    return md

def update_table_documentation(definitions, results):
    """Update table documentation with relevant test information"""
    
    # Group tests by table
    table_tests = {}
    
    for category_name, tests in definitions.items():
        for test_def in tests:
            test_def['category'] = category_name
            for table in test_def['tables']:
                if table not in table_tests:
                    table_tests[table] = []
                table_tests[table].append(test_def)
    
    # Update each table's documentation
    for table_name, tests in table_tests.items():
        doc_path = Path(f"docs/database/tables/{table_name}.md")
        
        if not doc_path.exists():
            print(f"  ⚠️  Table documentation not found: {table_name}")
            continue
        
        content = doc_path.read_text()
        
        # Check if Data Quality Notes section exists
        if "## Data Quality Notes" not in content:
            print(f"  ⚠️  No Data Quality Notes section in {table_name}")
            continue
        
        # Build quality tests section
        quality_section = "\n### Automated Data Quality Tests\n\n"
        quality_section += "This table is subject to the following automated quality checks:\n\n"
        
        for test in tests:
            # Check test result
            test_status = get_test_status(test['id'], results)
            status_icon = "✅" if test_status == "passed" else "❌"
            
            quality_section += f"**{status_icon} {test['id']}**: {test['name']}\n\n"
            quality_section += f"- **Severity**: {test['severity'].upper()}\n"
            quality_section += f"- **Status**: {test_status.upper()}\n"
            quality_section += f"- **Description**: {test['description']}\n\n"
        
        quality_section += "\nSee the [Data Quality Report](../../reports/data_quality_report.md) for details.\n\n"
        
        # Insert or replace quality tests section
        # Look for existing automated tests section
        pattern = r'### Automated Data Quality Tests.*?(?=\n##|\n---|\Z)'
        
        if re.search(pattern, content, re.DOTALL):
            # Replace existing section
            content = re.sub(pattern, quality_section.strip(), content, flags=re.DOTALL)
        else:
            # Insert after Data Quality Notes header
            content = content.replace(
                "## Data Quality Notes",
                "## Data Quality Notes" + quality_section
            )
        
        doc_path.write_text(content)
        print(f"  ✓ Updated {table_name}")

def extract_test_id(nodeid):
    """Extract test ID from pytest nodeid"""
    # Example: tests/data_quality/test_referential_integrity.py::test_ref_001
    match = re.search(r'test_(\w+_\d+)', nodeid)
    return match.group(1) if match else None

def find_test_definition(test_id, definitions):
    """Find test definition by ID"""
    for category_name, tests in definitions.items():
        for test in tests:
            if test['id'] == test_id:
                test['category'] = category_name
                return test
    return None

def get_test_status(test_id, results):
    """Get test status from results"""
    for test in results.get('tests', []):
        if test_id in test.get('nodeid', ''):
            return test.get('outcome', 'unknown')
    return 'unknown'

def main():
    print("Running data quality tests...")
    test_results = run_tests()
    
    print("\nLoading test definitions...")
    definitions = load_test_definitions()
    
    print("\nGenerating quality report...")
    # Load JSON results
    with open('tests/reports/results.json') as f:
        results = json.load(f)
    
    report = generate_markdown_report(results, definitions)
    
    # Save report
    report_path = Path("docs/reports/data_quality_report.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    print(f"✓ Report saved to {report_path}")
    
    print("\nUpdating table documentation...")
    update_table_documentation(definitions, results)
        
    _ = save_summary(results, definitions)
    print(f"✓ Summary saved")

    print("\n✓ Complete!")

def save_summary(results, definitions):
    """Save test summary as JSON for easy consumption"""
    
    summary = {
        'generated_at': datetime.now().isoformat(),
        'total_tests': 0,
        'passed': 0,
        'failed': 0,
        'by_severity': {
            'error': {'total': 0, 'passed': 0, 'failed': 0},
            'warning': {'total': 0, 'passed': 0, 'failed': 0}
        },
        'by_category': {}
    }
    
    # Count by category
    for category_name, tests in definitions.items():
        summary['by_category'][category_name] = {
            'total': len(tests),
            'passed': 0,
            'failed': 0
        }
        
        for test in tests:
            summary['total_tests'] += 1
            
            # Count by severity
            severity = test.get('severity', 'warning')
            summary['by_severity'][severity]['total'] += 1
            
            # Check if test passed
            test_status = get_test_status(test['id'], results)
            if test_status == 'passed':
                summary['passed'] += 1
                summary['by_category'][category_name]['passed'] += 1
                summary['by_severity'][severity]['passed'] += 1
            else:
                summary['failed'] += 1
                summary['by_category'][category_name]['failed'] += 1
                summary['by_severity'][severity]['failed'] += 1
    
    # Save summary
    summary_path = Path("tests/reports/summary.json")
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    return summary


if __name__ == "__main__":
    main()
    print(f"✓ Summary saved")