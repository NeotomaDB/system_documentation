"""
All data quality tests
Auto-generated from data_test_definition.yaml
"""
import pytest
import yaml
from pathlib import Path

def load_all_test_definitions():
    """Load all test definitions from YAML"""
    yaml_path = Path(__file__).parent / "data_test_definition.yaml"
    with open(yaml_path) as f:
        all_definitions = yaml.safe_load(f)
    
    # Flatten all categories into a single list
    all_tests = []
    for category, tests in all_definitions.items():
        for test in tests:
            test['category'] = category
            all_tests.append(test)
    
    return all_tests

@pytest.mark.parametrize('test_def', load_all_test_definitions(), ids=lambda t: t['id'])
def test_data_quality(cursor, test_def):
    """Run data quality test"""
    cursor.execute(test_def['query'])
    results = cursor.fetchall()
    
    if test_def['expect'] == 'empty':
        assert len(results) == 0, (
            f"\n{'='*80}\n"
            f"Test Failed: {test_def['name']} ({test_def['id']})\n"
            f"Category: {test_def['category']}\n"
            f"{'='*80}\n"
            f"Description: {test_def['description']}\n\n"
            f"Rationale: {test_def['rationale']}\n\n"
            f"Expected: No violations\n"
            f"Found: {len(results)} violations\n\n"
            f"Sample violations:\n"
            f"{'-'*80}\n"
        ) + "\n".join([str(row) for row in results[:10]])