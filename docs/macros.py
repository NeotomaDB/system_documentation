"""
MkDocs macros for dynamic database documentation
"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import yaml

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
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        return None

def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    """
    
    @env.macro
    def table_structure(table_name: str, schema: str = 'ndb'):
        """Generate table structure information"""
        conn = get_db_connection()
        if not conn:
            return "⚠️ Cannot connect to database"
        
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            # Get table comment
            cursor.execute("""
                SELECT obj_description(%s::regclass) as table_comment
            """, (f"{schema}.{table_name}",))
            
            result = cursor.fetchone()
            comment = result['table_comment'] if result and result['table_comment'] else "No description available"
            
            md = f"**Schema**: `{schema}` | **Table Comment**: {comment}\n\n"
            
            return md
        except Exception as e:
            return f"⚠️ Error fetching table structure: {str(e)}"
        finally:
            conn.close()
    
    @env.macro
    def table_stats(table_name: str, schema: str = 'ndb'):
        """Generate table statistics"""
        conn = get_db_connection()
        if not conn:
            return "⚠️ Cannot connect to database"
        
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            # Get row count and size
            cursor.execute(f"""
                SELECT 
                    (SELECT COUNT(*) FROM {schema}.{table_name}) as row_count,
                    pg_size_pretty(pg_total_relation_size(%s)) as total_size,
                    pg_size_pretty(pg_relation_size(%s)) as table_size,
                    pg_size_pretty(pg_indexes_size(%s)) as indexes_size
            """, (f"{schema}.{table_name}", f"{schema}.{table_name}", f"{schema}.{table_name}"))
            
            stats = cursor.fetchone()
            
            md = "| Metric | Value |\n|--------|-------|\n"
            md += f"| **Row Count** | {stats['row_count']:,} |\n"
            md += f"| **Total Size** | {stats['total_size']} |\n"
            md += f"| **Table Size** | {stats['table_size']} |\n"
            md += f"| **Indexes Size** | {stats['indexes_size']} |\n"
            
            return md
        except Exception as e:
            return f"⚠️ Error fetching statistics: {str(e)}"
        finally:
            conn.close()
    
    @env.macro
    def table_columns(table_name: str, schema: str = 'ndb'):
        """Generate detailed column information"""
        conn = get_db_connection()
        if not conn:
            return "⚠️ Cannot connect to database"
        
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            cursor.execute("""
                SELECT 
                    c.column_name,
                    c.data_type,
                    c.character_maximum_length,
                    c.is_nullable,
                    c.column_default,
                    col_description(%s::regclass, c.ordinal_position) as column_comment,
                    (
                        SELECT string_agg(tc.constraint_type, ', ')
                        FROM information_schema.table_constraints tc
                        JOIN information_schema.constraint_column_usage ccu 
                            ON tc.constraint_name = ccu.constraint_name
                            AND tc.table_schema = ccu.table_schema
                        WHERE tc.table_schema = c.table_schema
                            AND tc.table_name = c.table_name
                            AND ccu.column_name = c.column_name
                    ) as constraints
                FROM information_schema.columns c
                WHERE c.table_schema = %s
                    AND c.table_name = %s
                ORDER BY c.ordinal_position
            """, (f"{schema}.{table_name}", schema, table_name))
            
            columns = cursor.fetchall()
            
            if not columns:
                return f"⚠️ Table `{table_name}` not found in schema `{schema}`"
            
            md = "| Column | Type | Nullable | Default | Constraints | Description |\n"
            md += "|--------|------|----------|---------|-------------|-------------|\n"
            
            for col in columns:
                # Format type with length if applicable
                col_type = col['data_type']
                if col['character_maximum_length']:
                    col_type += f"({col['character_maximum_length']})"
                
                # Handle nullable
                nullable = "✓" if col['is_nullable'] == 'YES' else "✗"
                
                # Handle default
                default = col['column_default'] if col['column_default'] else "-"
                if len(default) > 30:
                    default = default[:27] + "..."
                
                # Handle constraints
                constraints = col['constraints'] if col['constraints'] else "-"
                
                # Handle description
                description = col['column_comment'] if col['column_comment'] else ""
                
                md += f"| `{col['column_name']}` | {col_type} | {nullable} | "
                md += f"`{default}` | {constraints} | {description} |\n"
            
            return md
        except Exception as e:
            return f"⚠️ Error fetching columns: {str(e)}"
        finally:
            conn.close()
    
    @env.macro
    def all_tables_list(schema: str = 'ndb'):
        """Generate list of all tables with basic info"""
        conn = get_db_connection()
        if not conn:
            return "⚠️ Cannot connect to database"
        
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            
            cursor.execute("""
                SELECT 
                    t.table_name,
                    obj_description((quote_ident(t.table_schema)||'.'||quote_ident(t.table_name))::regclass) as description,
                    (SELECT COUNT(*) 
                     FROM information_schema.columns c 
                     WHERE c.table_schema = t.table_schema 
                     AND c.table_name = t.table_name) as column_count,
                    pg_size_pretty(pg_total_relation_size(
                        quote_ident(t.table_schema)||'.'||quote_ident(t.table_name)
                    )) as size
                FROM information_schema.tables t
                WHERE t.table_schema = %s
                    AND t.table_type = 'BASE TABLE'
                ORDER BY t.table_name
            """, (schema,))
            
            tables = cursor.fetchall()
            
            md = "| Table | Description | Columns | Size |\n"
            md += "|-------|-------------|---------|------|\n"
            
            for table in tables:
                # Check if documentation exists
                doc_path = Path(f"docs/database/tables/{table['table_name']}.md")
                table_link = f"[`{table['table_name']}`](tables/{table['table_name']}.md)"
                if not doc_path.exists():
                    table_link += " ⚠️"
                
                description = table['description'] if table['description'] else "No description"
                if len(description) > 80:
                    description = description[:77] + "..."
                
                md += f"| {table_link} | {description} | "
                md += f"{table['column_count']} | {table['size']} |\n"
            
            return md
        except Exception as e:
            return f"⚠️ Error fetching table list: {str(e)}"
        finally:
            conn.close()
    
    @env.macro
    def last_validated():
        """Return current date as last validated date"""
        return datetime.now().strftime("%Y-%m-%d")
    
    @env.macro
    def doc_status(table_name: str):
        """Check documentation status from frontmatter"""
        doc_path = Path(f"docs/database/tables/{table_name}.md")
        
        if not doc_path.exists():
            return "❌ Missing"
        
        try:
            with open(doc_path, 'r') as f:
                content = f.read()
                # Simple frontmatter parsing
                if content.startswith('---'):
                    frontmatter = content.split('---')[1]
                    if 'status: complete' in frontmatter:
                        return "✅ Complete"
                    elif 'status: review' in frontmatter:
                        return "🔄 In Review"
                    else:
                        return "📝 Draft"
        except:
            pass
        
        return "❓ Unknown"
    
    @env.macro
    def api_version():
        """Get API version from OpenAPI spec"""
        import yaml
        openapi_path = Path(__file__).parent / "api" / "openapi.yaml"
        
        if not openapi_path.exists():
            return "Unknown"
        
        try:
            with open(openapi_path) as f:
                spec = yaml.safe_load(f)
                return spec.get('info', {}).get('version', 'Unknown')
        except:
            return "Unknown"
    
    @env.macro
    def api_table_mapping():
        """Generate mapping between API endpoints and database tables"""
        import yaml
        import re
        
        openapi_path = Path(__file__).parent / "api" / "openapi.yaml"
        
        if not openapi_path.exists():
            return "⚠️ OpenAPI specification not found"
        
        try:
            with open(openapi_path) as f:
                spec = yaml.safe_load(f)
            
            # Build mapping from endpoints to tables
            # This requires some parsing of your OpenAPI spec
            # Adjust based on your actual spec structure
            
            mapping = {}
            
            for path, methods in spec.get('paths', {}).items():
                for method, details in methods.items():
                    if method.startswith('x-'):  # Skip extensions
                        continue
                    
                    # Try to extract table name from description or tags
                    # This is a simple heuristic - adjust based on your spec
                    description = details.get('description', '')
                    summary = details.get('summary', '')
                    tags = details.get('tags', [])
                    
                    # Look for table references in description
                    # Pattern: looks for markdown links like [table_name](...)
                    table_pattern = r'\[`?(\w+)`?\]\([^\)]*tables/(\w+)\.md\)'
                    matches = re.findall(table_pattern, description)
                    
                    if not matches:
                        # Try extracting from tags (if you use table names as tags)
                        for tag in tags:
                            if tag not in mapping:
                                mapping[tag] = []
                            mapping[tag].append({
                                'method': method.upper(),
                                'path': path,
                                'summary': summary
                            })
                    else:
                        for _, table_name in matches:
                            if table_name not in mapping:
                                mapping[table_name] = []
                            mapping[table_name].append({
                                'method': method.upper(),
                                'path': path,
                                'summary': summary
                            })
            
            # Generate markdown table
            if not mapping:
                return "⚠️ No table mappings found. Ensure your OpenAPI spec includes table references."
            
            md = ""
            for table_name in sorted(mapping.keys()):
                md += f"\n## Table: [`{table_name}`](../../database/tables/{table_name}.md)\n\n"
                md += "| Method | Endpoint | Description |\n"
                md += "|--------|----------|-------------|\n"
                
                for endpoint in mapping[table_name]:
                    md += f"| `{endpoint['method']}` | `{endpoint['path']}` | {endpoint['summary']} |\n"
                
                md += "\n"
            
            return md
            
        except Exception as e:
            return f"⚠️ Error parsing OpenAPI spec: {str(e)}"
