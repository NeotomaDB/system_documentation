"""
Generate initial documentation files for all database tables.
This script creates a markdown file for each table with all required sections.
"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import argparse

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

DOCS_PATH = Path(__file__).parent.parent / "docs" / "database" / "tables"


def get_db_connection():
    """Create database connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None


def get_all_tables(conn, schema='ndb'):
    """Get list of all tables in the schema"""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    cursor.execute("""
        SELECT 
            t.table_name,
            obj_description((quote_ident(t.table_schema)||'.'||quote_ident(t.table_name))::regclass) as table_comment,
            (SELECT COUNT(*) 
             FROM information_schema.columns c 
             WHERE c.table_schema = t.table_schema 
             AND c.table_name = t.table_name) as column_count
        FROM information_schema.tables t
        WHERE t.table_schema = %s
            AND t.table_type = 'BASE TABLE'
        ORDER BY t.table_name
    """, (schema,))
    
    return cursor.fetchall()


def get_table_columns(conn, table_name, schema='ndb'):
    """Get column information for a table"""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    cursor.execute("""
        SELECT 
            c.column_name,
            c.data_type,
            c.character_maximum_length,
            c.is_nullable,
            c.column_default,
            col_description(%s::regclass, c.ordinal_position) as column_comment
        FROM information_schema.columns c
        WHERE c.table_schema = %s
            AND c.table_name = %s
        ORDER BY c.ordinal_position
    """, (f"{schema}.{table_name}", schema, table_name))
    
    return cursor.fetchall()


def get_foreign_keys(conn, table_name, schema='ndb'):
    """Get foreign key relationships for a table"""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    cursor.execute("""
        SELECT
            kcu.column_name,
            ccu.table_name AS foreign_table_name,
            ccu.column_name AS foreign_column_name
        FROM information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
            ON tc.constraint_name = kcu.constraint_name
            AND tc.table_schema = kcu.table_schema
        JOIN information_schema.constraint_column_usage AS ccu
            ON ccu.constraint_name = tc.constraint_name
            AND ccu.table_schema = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
            AND tc.table_schema = %s
            AND tc.table_name = %s
    """, (schema, table_name))
    
    return cursor.fetchall()


def get_primary_keys(conn, table_name, schema='ndb'):
    """Get primary key columns for a table"""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    cursor.execute("""
        SELECT kcu.column_name
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
            ON tc.constraint_name = kcu.constraint_name
            AND tc.table_schema = kcu.table_schema
        WHERE tc.constraint_type = 'PRIMARY KEY'
            AND tc.table_schema = %s
            AND tc.table_name = %s
        ORDER BY kcu.ordinal_position
    """, (schema, table_name))
    
    return [row['column_name'] for row in cursor.fetchall()]


def generate_sample_queries(table_name, columns, primary_keys, foreign_keys):
    """Generate sample SQL queries for the table"""
    queries = []
    
    # Basic SELECT
    queries.append({
        'title': 'Basic Selection',
        'sql': f"""-- Get recent records from {table_name}
SELECT *
FROM {table_name}
ORDER BY {primary_keys[0] if primary_keys else columns[0]['column_name']} DESC
LIMIT 10;""",
        'purpose': f'Retrieve the 10 most recent records from {table_name}'
    })
    
    # COUNT query
    queries.append({
        'title': 'Count Records',
        'sql': f"""-- Count total records
SELECT COUNT(*) as total_records
FROM {table_name};""",
        'purpose': f'Get the total number of records in {table_name}'
    })
    
    # If there are date columns, add a date-filtered query
    date_columns = [col for col in columns if 'date' in col['data_type'].lower() or 'timestamp' in col['data_type'].lower()]
    if date_columns:
        date_col = date_columns[0]['column_name']
        queries.append({
            'title': 'Filter by Date Range',
            'sql': f"""-- Get records within a date range
SELECT *
FROM {table_name}
WHERE {date_col} >= '2024-01-01'
  AND {date_col} < '2025-01-01'
ORDER BY {date_col} DESC;""",
            'purpose': f'Retrieve records from {table_name} within a specific date range'
        })
    
    # If there are foreign keys, add a JOIN example
    if foreign_keys:
        fk = foreign_keys[0]
        queries.append({
            'title': f'Join with {fk["foreign_table_name"]}',
            'sql': f"""-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM {table_name} t1
INNER JOIN {fk['foreign_table_name']} t2 
    ON t1.{fk['column_name']} = t2.{fk['foreign_column_name']}
LIMIT 100;""",
            'purpose': f'Retrieve {table_name} records with related data from {fk["foreign_table_name"]}'
        })
    
    # Add a GROUP BY example if appropriate
    if len(columns) > 2:
        group_col = columns[1]['column_name']  # Second column for variety
        queries.append({
            'title': 'Aggregate Data',
            'sql': f"""-- Aggregate records by {group_col}
SELECT 
    {group_col},
    COUNT(*) as count
FROM {table_name}
GROUP BY {group_col}
ORDER BY count DESC
LIMIT 10;""",
            'purpose': f'Count records grouped by {group_col}'
        })
    
    return queries


def generate_markdown(table_info, columns, foreign_keys, primary_keys):
    """Generate markdown content for a table"""
    table_name = table_info['table_name']
    table_comment = table_info['table_comment'] or "No description available in database."
    
    # Generate queries
    queries = generate_sample_queries(table_name, columns, primary_keys, foreign_keys)
    
    # Build markdown
    md = f"""---
title: {table_name.replace('_', ' ').title()}
description: {table_comment[:100]}
status: draft
last_validated: {datetime.now().strftime('%Y-%m-%d')}
---

# Table: `ndb.{table_name}`

## Description

{table_comment}

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2e{table_name}-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/{table_name}.html)

{{{{ table_structure("{table_name}") }}}}

## Statistics

{{{{ table_stats("{table_name}") }}}}

## Relationships

"""
    
    # Add primary key info
    if primary_keys:
        md += f"**Primary Key**: `{', '.join(primary_keys)}`\n\n"
    
    # Add foreign key relationships
    if foreign_keys:
        md += "**Foreign Keys**:\n\n"
        for fk in foreign_keys:
            md += f"- `{fk['column_name']}` → [`{fk['foreign_table_name']}.{fk['foreign_column_name']}`]({fk['foreign_table_name']}.md)\n"
        md += "\n"
    else:
        md += "No foreign key relationships.\n\n"
    
    # Add reverse relationships placeholder
    md += """**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

"""
    
    # Data dictionary
    md += f"""## Data Dictionary

{{{{ table_columns("{table_name}") }}}}

**TODO**: Review column descriptions and add comments where missing.

"""
    
    # Usage examples
    md += "## Usage Examples\n\n"
    
    for i, query in enumerate(queries, 1):
        md += f"### Example {i}: {query['title']}\n\n"
        md += f"```sql\n{query['sql']}\n```\n\n"
        md += f"**Purpose**: {query['purpose']}\n\n"
    
    md += """**TODO**: Add more specific examples relevant to common research questions or operational tasks.

## Data Quality Notes

**TODO**: Document:
- Known data quality issues
- Validation rules
- Expected data ranges
- Update frequency and mechanisms
- Any ETL processes that populate this table

## Maintenance

- **Data Owner**: TODO: Assign owner
- **Update Frequency**: TODO: Document frequency
- **Last Major Schema Change**: TODO: Document when schema last changed

## Related Documentation

**TODO**: Link to:
- Related API endpoints
- Data collection procedures
- Analysis notebooks or reports that use this table
- External ontologies or standards

---
"""
    
    return md


def generate_docs_for_table(conn, table_info, force=False):
    """Generate documentation file for a single table"""
    table_name = table_info['table_name']
    doc_file = DOCS_PATH / f"{table_name}.md"
    
    # Check if file exists
    if doc_file.exists() and not force:
        print(f"  ⊗ Skipping {table_name} (file exists, use --force to overwrite)")
        return False
    
    # Get table details
    columns = get_table_columns(conn, table_name)
    foreign_keys = get_foreign_keys(conn, table_name)
    primary_keys = get_primary_keys(conn, table_name)
    
    # Generate markdown
    markdown = generate_markdown(table_info, columns, foreign_keys, primary_keys)
    
    # Write to file
    with open(doc_file, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"  ✓ Generated documentation for {table_name}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Generate documentation files for database tables'
    )
    parser.add_argument(
        '--schema',
        default='ndb',
        help='Database schema to document (default: ndb)'
    )
    parser.add_argument(
        '--table',
        help='Generate documentation for a specific table only'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Overwrite existing documentation files'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be generated without creating files'
    )
    
    args = parser.parse_args()
    
    # Ensure docs directory exists
    DOCS_PATH.mkdir(parents=True, exist_ok=True)
    
    # Connect to database
    conn = get_db_connection()
    if not conn:
        return 1
    
    try:
        # Get tables
        if args.table:
            # Get specific table
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""
                SELECT 
                    table_name,
                    obj_description((quote_ident(table_schema)||'.'||quote_ident(table_name))::regclass) as table_comment,
                    (SELECT COUNT(*) 
                     FROM information_schema.columns c 
                     WHERE c.table_schema = %s 
                     AND c.table_name = %s) as column_count
                FROM information_schema.tables
                WHERE table_schema = %s
                    AND table_name = %s
                    AND table_type = 'BASE TABLE'
            """, (args.schema, args.table, args.schema, args.table))
            
            tables = cursor.fetchall()
            if not tables:
                print(f"✗ Table '{args.table}' not found in schema '{args.schema}'")
                return 1
        else:
            # Get all tables
            tables = get_all_tables(conn, args.schema)
        
        print(f"\nFound {len(tables)} table(s) in schema '{args.schema}'")
        
        if args.dry_run:
            print("\n=== DRY RUN MODE ===")
            print("\nWould generate documentation for:")
            for table in tables:
                doc_file = DOCS_PATH / f"{table['table_name']}.md"
                status = "EXISTS" if doc_file.exists() else "NEW"
                if doc_file.exists() and args.force:
                    status = "OVERWRITE"
                print(f"  [{status}] {table['table_name']}")
            return 0
        
        # Generate documentation
        print("\nGenerating documentation files...")
        generated = 0
        skipped = 0
        
        for table_info in tables:
            if generate_docs_for_table(conn, table_info, args.force):
                generated += 1
            else:
                skipped += 1
        
        print(f"\n✓ Complete!")
        print(f"  Generated: {generated}")
        print(f"  Skipped: {skipped}")
        print(f"  Total: {len(tables)}")
        print(f"\nDocumentation files written to: {DOCS_PATH}")
        
        return 0
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    finally:
        conn.close()


if __name__ == "__main__":
    exit(main())
