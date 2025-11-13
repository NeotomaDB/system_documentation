---
title: Relativeages
description: Lookup table of RelativeAges. Table is referenced by the RelativeChronology table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.relativeages`

## Description

Lookup table of RelativeAges. Table is referenced by the RelativeChronology table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2erelativeages-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/relativeages.html)

{{ table_structure("relativeages") }}

## Statistics

{{ table_stats("relativeages") }}

## Relationships

**Primary Key**: `relativeageid`

**Foreign Keys**:

- `relativeagescaleid` → [`relativeagescales.relativeagescaleid`](relativeagescales.md)
- `relativeageunitid` → [`relativeageunits.relativeageunitid`](relativeageunits.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("relativeages") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from relativeages
SELECT *
FROM relativeages
ORDER BY relativeageid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from relativeages

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM relativeages;
```

**Purpose**: Get the total number of records in relativeages

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM relativeages
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from relativeages within a specific date range

### Example 4: Join with relativeagescales

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM relativeages t1
INNER JOIN relativeagescales t2 
    ON t1.relativeagescaleid = t2.relativeagescaleid
LIMIT 100;
```

**Purpose**: Retrieve relativeages records with related data from relativeagescales

### Example 5: Aggregate Data

```sql
-- Aggregate records by relativeageunitid
SELECT 
    relativeageunitid,
    COUNT(*) as count
FROM relativeages
GROUP BY relativeageunitid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by relativeageunitid

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
