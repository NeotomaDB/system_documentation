---
title: Datasettypes
description: Lookup table for Dataset Types. Table is referenced by the Datasets table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.datasettypes`

## Description

Lookup table for Dataset Types. Table is referenced by the Datasets table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2edatasettypes-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/datasettypes.html)

{{ table_structure("datasettypes") }}

## Statistics

{{ table_stats("datasettypes") }}

## Relationships

**Primary Key**: `datasettypeid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("datasettypes") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from datasettypes
SELECT *
FROM datasettypes
ORDER BY datasettypeid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from datasettypes

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM datasettypes;
```

**Purpose**: Get the total number of records in datasettypes

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM datasettypes
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from datasettypes within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by datasettype
SELECT 
    datasettype,
    COUNT(*) as count
FROM datasettypes
GROUP BY datasettype
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by datasettype

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
