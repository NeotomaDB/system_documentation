---
title: Aggregatechronologies
description: This table stores metadata for Aggregate Chronologies. An Aggregate Chronology refers to an explicit
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.aggregatechronologies`

## Description

This table stores metadata for Aggregate Chronologies. An Aggregate Chronology refers to an explicit chronology assigned to a sample Aggregate. The individual Aggregate Samples have ages assigned in the AggregateSampleAges table. An Aggregate Chronology would be used, for example, for a set of packrat middens assigned to an AggregateDataset. The Aggregate Chronology is analogous to the Chronology assigned to samples from a single Collection Unit.
An Aggregate may have more than one Aggregate Chronology, for example one in radiocarbon years and another in calibrated radiocarbon years. One Aggregate Chronology per Age Type may be designated the default, which is the Aggregate Chronology currently preferred by the database stewards.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eaggregatechronologies-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/aggregatechronologies.html)

{{ table_structure("aggregatechronologies") }}

## Statistics

{{ table_stats("aggregatechronologies") }}

## Relationships

**Primary Key**: `aggregatechronid`

**Foreign Keys**:

- `agetypeid` → [`agetypes.agetypeid`](agetypes.md)
- `aggregatedatasetid` → [`aggregatedatasets.aggregatedatasetid`](aggregatedatasets.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("aggregatechronologies") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from aggregatechronologies
SELECT *
FROM aggregatechronologies
ORDER BY aggregatechronid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from aggregatechronologies

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM aggregatechronologies;
```

**Purpose**: Get the total number of records in aggregatechronologies

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM aggregatechronologies
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from aggregatechronologies within a specific date range

### Example 4: Join with agetypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM aggregatechronologies t1
INNER JOIN agetypes t2 
    ON t1.agetypeid = t2.agetypeid
LIMIT 100;
```

**Purpose**: Retrieve aggregatechronologies records with related data from agetypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by aggregatedatasetid
SELECT 
    aggregatedatasetid,
    COUNT(*) as count
FROM aggregatechronologies
GROUP BY aggregatedatasetid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by aggregatedatasetid

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
