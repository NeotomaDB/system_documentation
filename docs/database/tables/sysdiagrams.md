---
title: Sysdiagrams
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.sysdiagrams`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esysdiagrams-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/sysdiagrams.html)

{{ table_structure("sysdiagrams") }}

## Statistics

{{ table_stats("sysdiagrams") }}

## Relationships

**Primary Key**: `diagram_id`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("sysdiagrams") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from sysdiagrams
SELECT *
FROM sysdiagrams
ORDER BY diagram_id DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from sysdiagrams

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM sysdiagrams;
```

**Purpose**: Get the total number of records in sysdiagrams

### Example 3: Aggregate Data

```sql
-- Aggregate records by principal_id
SELECT 
    principal_id,
    COUNT(*) as count
FROM sysdiagrams
GROUP BY principal_id
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by principal_id

**TODO**: Add more specific examples relevant to common research questions or operational tasks.

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
