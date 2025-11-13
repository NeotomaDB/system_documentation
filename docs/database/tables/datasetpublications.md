---
title: Datasetpublications
description: This table lists the publications for datasets.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.datasetpublications`

## Description

This table lists the publications for datasets.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2edatasetpublications-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/datasetpublications.html)

{{ table_structure("datasetpublications") }}

## Statistics

{{ table_stats("datasetpublications") }}

## Relationships

**Primary Key**: `datasetid, publicationid`

**Foreign Keys**:

- `datasetid` → [`datasets.datasetid`](datasets.md)
- `publicationid` → [`publications.publicationid`](publications.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("datasetpublications") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from datasetpublications
SELECT *
FROM datasetpublications
ORDER BY datasetid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from datasetpublications

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM datasetpublications;
```

**Purpose**: Get the total number of records in datasetpublications

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM datasetpublications
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from datasetpublications within a specific date range

### Example 4: Join with datasets

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM datasetpublications t1
INNER JOIN datasets t2 
    ON t1.datasetid = t2.datasetid
LIMIT 100;
```

**Purpose**: Retrieve datasetpublications records with related data from datasets

### Example 5: Aggregate Data

```sql
-- Aggregate records by publicationid
SELECT 
    publicationid,
    COUNT(*) as count
FROM datasetpublications
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
