---
title: Aggregatesampleages
description: This table stores the links to the ages of samples in an Aggregate Dataset. The table is necessary b
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.aggregatesampleages`

## Description

This table stores the links to the ages of samples in an Aggregate Dataset. The table is necessary because samples may be from Collection Units with multiple chronologies, and this table stores the links to the sample ages desired for the Aggregate Dataset.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eaggregatesampleages-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/aggregatesampleages.html)

{{ table_structure("aggregatesampleages") }}

## Statistics

{{ table_stats("aggregatesampleages") }}

## Relationships

**Primary Key**: `aggregatedatasetid, aggregatechronid, sampleageid`

**Foreign Keys**:

- `aggregatechronid` → [`aggregatechronologies.aggregatechronid`](aggregatechronologies.md)
- `aggregatedatasetid` → [`aggregatedatasets.aggregatedatasetid`](aggregatedatasets.md)
- `sampleageid` → [`sampleages.sampleageid`](sampleages.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("aggregatesampleages") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from aggregatesampleages
SELECT *
FROM aggregatesampleages
ORDER BY aggregatedatasetid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from aggregatesampleages

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM aggregatesampleages;
```

**Purpose**: Get the total number of records in aggregatesampleages

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM aggregatesampleages
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from aggregatesampleages within a specific date range

### Example 4: Join with aggregatechronologies

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM aggregatesampleages t1
INNER JOIN aggregatechronologies t2 
    ON t1.aggregatechronid = t2.aggregatechronid
LIMIT 100;
```

**Purpose**: Retrieve aggregatesampleages records with related data from aggregatechronologies

### Example 5: Aggregate Data

```sql
-- Aggregate records by aggregatechronid
SELECT 
    aggregatechronid,
    COUNT(*) as count
FROM aggregatesampleages
GROUP BY aggregatechronid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by aggregatechronid

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
