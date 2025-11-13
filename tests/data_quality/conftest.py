"""
Pytest configuration and fixtures for data quality tests
"""
import pytest
import psycopg2
from psycopg2.extras import RealDictCursor
import yaml
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def db_connection():
    """Create database connection for tests"""
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def test_definitions():
    """Load test definitions from YAML"""
    yaml_path = Path(__file__).parent / "data_test_definition.yaml"
    with open(yaml_path) as f:
        return yaml.safe_load(f)

@pytest.fixture
def cursor(db_connection):
    """Create cursor for each test"""
    cur = db_connection.cursor(cursor_factory=RealDictCursor)
    yield cur
    cur.close()

def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "severity_error: marks tests as error severity"
    )
    config.addinivalue_line(
        "markers", "severity_warning: marks tests as warning severity"
    )
    config.addinivalue_line(
        "markers", "category_referential: referential integrity tests"
    )
    config.addinivalue_line(
        "markers", "category_completeness: data completeness tests"
    )
    config.addinivalue_line(
        "markers", "category_validity: data validity tests"
    )
    config.addinivalue_line(
        "markers", "category_business: business rule tests"
    )