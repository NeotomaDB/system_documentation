"""
Referential integrity tests
Auto-generated from test_definitions.yaml
"""
import pytest
from pathlib import Path
import yaml

def generate_test_function(test_def):
    """Generate a test function from test definition"""
    def test_func(cursor):
        # Execute the query
        cursor.execute(test_def['query'])
        results = cursor.fetchall()
        
        # Check expectation
        if test_def['expect'] == 'empty':
            assert len(results) == 0, (
                f"Test {test_def['id']}: {test_def['name']} failed\n"
                f"Expected no results, but found {len(results)} rows:\n"
                f"{results[:5]}"  # Show first 5 rows
            )
        else:
            # Could extend for other expectations
            pass
    
    # Set test metadata
    test_func.__name__ = f"test_{test_def['id']}_{test_def['name']}"
    test_func.__doc__ = test_def['description']
    
    return test_func

# Load test definitions and generate test functions
def pytest_generate_tests(metafunc):
    """Dynamically generate tests from YAML definitions"""
    if 'test_def' in metafunc.fixturenames:
        # Load definitions
        yaml_path = Path(__file__).parent / "data_test_definition.yaml"
        with open(yaml_path) as f:
            definitions = yaml.safe_load(f)
        
        # Get tests for this category
        category = metafunc.module.__name__.split('_')[-1]  # e.g., 'referential'
        
        if category == 'integrity':
            category = 'referential_integrity'
        
        tests = definitions.get(category, {})
        
        # Parametrize with test definitions
        metafunc.parametrize('test_def', tests, ids=[t['id'] for t in tests])

def test_referential_integrity(cursor, test_def):
    """Run referential integrity test"""
    cursor.execute(test_def['query'])
    results = cursor.fetchall()
    
    if test_def['expect'] == 'empty':
        assert len(results) == 0, (
            f"\n{'='*80}\n"
            f"Test Failed: {test_def['name']} ({test_def['id']})\n"
            f"{'='*80}\n"
            f"Description: {test_def['description']}\n\n"
            f"Rationale: {test_def['rationale']}\n\n"
            f"Expected: No violations\n"
            f"Found: {len(results)} violations\n\n"
            f"Sample violations:\n"
            f"{'-'*80}\n"
        ) + "\n".join([str(row) for row in results[:10]])