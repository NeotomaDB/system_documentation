"""
Add API endpoint references to table documentation
"""
import yaml
import re
from pathlib import Path
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Load environment variables
load_dotenv()

# Database connection config
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
}

def get_db_connection():
    """Create database connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None


def parse_openapi():
    """Parse OpenAPI spec and extract table references"""
    openapi_path = Path("docs/api/openapi.yaml")
    
    with open(openapi_path) as f:
        spec = yaml.safe_load(f)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'ndb' 
        AND table_type = 'BASE TABLE'
    """)

    actual_tables = set([row[0] for row in cursor.fetchall()])
    
    conn.close()

    table_endpoints = {}
    
    for path, methods in spec.get('paths', {}).items():
        for method, details in methods.items():
            if method.startswith('x-'):
                continue
            description = details.get('description', '')
            summary = details.get('summary', '')
            print(description)
            # Find table references in description
            table_pattern = r'`(\w+)`'
            tables = re.findall(table_pattern, description + summary)
            print(tables)
            for table in tables:
                if table not in table_endpoints:
                    table_endpoints[table] = []
                table_endpoints[table].append({
                    'method': method.upper(),
                    'path': path,
                    'summary': summary
                })
    
    return table_endpoints

def update_table_doc(table_name, endpoints):
    """Add API endpoints section to table documentation"""
    doc_path = Path(f"docs/database/tables/{table_name}.md")
    
    if not doc_path.exists():
        return False
    
    content = doc_path.read_text()
    
    # Check if API section already exists
    if "## API Endpoints" in content:
        print(f"  ⊗ {table_name} already has API section")
        return False
    
    # Build API section
    api_section = "\n## API Endpoints\n\n"
    api_section += "This table is accessed through the following API endpoints:\n\n"
    api_section += "| Method | Endpoint | Description |\n"
    api_section += "|--------|----------|-------------|\n"
    
    for endpoint in endpoints:
        api_section += f"| `{endpoint['method']}` | `{endpoint['path']}` | {endpoint['summary']} |\n"
    
    api_section += "\nSee the [API documentation](../../api/index.md) for details.\n"
    
    # Insert before "Related Documentation" section
    if "## Related Documentation" in content:
        content = content.replace("## Related Documentation", api_section + "\n## Related Documentation")
    else:
        # Insert before final separator
        content = content.replace("\n---\n", api_section + "\n---\n")
    
    doc_path.write_text(content)
    print(f"  ✓ Added API section to {table_name}")
    return True

def main():
    print("Parsing OpenAPI specification...")
    table_endpoints = parse_openapi()
    
    print(f"\nFound API references to {len(table_endpoints)} tables")
    print("\nUpdating table documentation...")
    
    updated = 0
    for table_name, endpoints in table_endpoints.items():
        if update_table_doc(table_name, endpoints):
            updated += 1
    
    print(f"\n✓ Updated {updated} table documentation files")

if __name__ == "__main__":
    main()