---
title: Aggregatesamples
description: This table stores the samples in Aggregate Datasets.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.aggregatesamples`

## Description

This table stores the samples in Aggregate Datasets.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eaggregatesamples-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/aggregatesamples.html)

{{ table_structure("aggregatesamples") }}

## Statistics

{{ table_stats("aggregatesamples") }}

## Relationships

**Primary Key**: `aggregatedatasetid, sampleid`

**Foreign Keys**:

- `aggregatedatasetid` → [`aggregatedatasets.aggregatedatasetid`](aggregatedatasets.md)
- `sampleid` → [`samples.sampleid`](samples.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("aggregatesamples") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from aggregatesamples
SELECT *
FROM aggregatesamples
ORDER BY aggregatedatasetid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from aggregatesamples

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM aggregatesamples;
```

**Purpose**: Get the total number of records in aggregatesamples

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM aggregatesamples
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from aggregatesamples within a specific date range

### Example 4: Join with aggregatedatasets

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM aggregatesamples t1
INNER JOIN aggregatedatasets t2 
    ON t1.aggregatedatasetid = t2.aggregatedatasetid
LIMIT 100;
```

**Purpose**: Retrieve aggregatesamples records with related data from aggregatedatasets

### Example 5: Aggregate Data

```sql
-- Aggregate records by sampleid
SELECT 
    sampleid,
    COUNT(*) as count
FROM aggregatesamples
GROUP BY sampleid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by sampleid

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
