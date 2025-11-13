---
title: Relativeagepublications
description: This table stores Publications in which Relative Ages are reported for CollectionUnits.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.relativeagepublications`

## Description

This table stores Publications in which Relative Ages are reported for CollectionUnits.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2erelativeagepublications-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/relativeagepublications.html)

{{ table_structure("relativeagepublications") }}

## Statistics

{{ table_stats("relativeagepublications") }}

## Relationships

**Primary Key**: `relativeageid, publicationid`

**Foreign Keys**:

- `publicationid` → [`publications.publicationid`](publications.md)
- `relativeageid` → [`relativeages.relativeageid`](relativeages.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("relativeagepublications") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from relativeagepublications
SELECT *
FROM relativeagepublications
ORDER BY relativeageid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from relativeagepublications

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM relativeagepublications;
```

**Purpose**: Get the total number of records in relativeagepublications

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM relativeagepublications
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from relativeagepublications within a specific date range

### Example 4: Join with publications

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM relativeagepublications t1
INNER JOIN publications t2 
    ON t1.publicationid = t2.publicationid
LIMIT 100;
```

**Purpose**: Retrieve relativeagepublications records with related data from publications

### Example 5: Aggregate Data

```sql
-- Aggregate records by publicationid
SELECT 
    publicationid,
    COUNT(*) as count
FROM relativeagepublications
GROUP BY publicationid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by publicationid

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
