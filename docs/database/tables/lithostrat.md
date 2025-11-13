---
title: Lithostrat
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.lithostrat`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2elithostrat-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/lithostrat.html)

{{ table_structure("lithostrat") }}

## Statistics

{{ table_stats("lithostrat") }}

## Relationships

**Primary Key**: `lithostratid`

**Foreign Keys**:

- `higherlithostratid` → [`lithostrat.lithostratid`](lithostrat.md)
- `lithostratunitid` → [`lithostratunits.lithostratunitid`](lithostratunits.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("lithostrat") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from lithostrat
SELECT *
FROM lithostrat
ORDER BY lithostratid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from lithostrat

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM lithostrat;
```

**Purpose**: Get the total number of records in lithostrat

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM lithostrat
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from lithostrat within a specific date range

### Example 4: Join with lithostrat

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM lithostrat t1
INNER JOIN lithostrat t2 
    ON t1.higherlithostratid = t2.lithostratid
LIMIT 100;
```

**Purpose**: Retrieve lithostrat records with related data from lithostrat

### Example 5: Aggregate Data

```sql
-- Aggregate records by lithostratunitid
SELECT 
    lithostratunitid,
    COUNT(*) as count
FROM lithostrat
GROUP BY lithostratunitid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by lithostratunitid

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
