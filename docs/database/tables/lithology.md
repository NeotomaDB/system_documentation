---
title: Lithology
description: This table stores the lithologic descriptions of Collection Units.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.lithology`

## Description

This table stores the lithologic descriptions of Collection Units.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2elithology-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/lithology.html)

{{ table_structure("lithology") }}

## Statistics

{{ table_stats("lithology") }}

## Relationships

**Primary Key**: `lithologyid`

**Foreign Keys**:

- `collectionunitid` → [`collectionunits.collectionunitid`](collectionunits.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("lithology") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from lithology
SELECT *
FROM lithology
ORDER BY lithologyid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from lithology

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM lithology;
```

**Purpose**: Get the total number of records in lithology

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM lithology
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from lithology within a specific date range

### Example 4: Join with collectionunits

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM lithology t1
INNER JOIN collectionunits t2 
    ON t1.collectionunitid = t2.collectionunitid
LIMIT 100;
```

**Purpose**: Retrieve lithology records with related data from collectionunits

### Example 5: Aggregate Data

```sql
-- Aggregate records by collectionunitid
SELECT 
    collectionunitid,
    COUNT(*) as count
FROM lithology
GROUP BY collectionunitid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by collectionunitid

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
