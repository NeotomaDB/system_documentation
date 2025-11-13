---
title: Aggregatedatasets
description: Aggregate Datasets are aggregates of samples of a particular data type. Some examples:  
* Plant mac
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.aggregatedatasets`

## Description

Aggregate Datasets are aggregates of samples of a particular data type. Some examples:  
* Plant macrofossil samples from a group of packrat middens collected from a particular valley, mountain range, or other similarly defined geographic area. Each midden is from a different Site or Collection Unit, but they are grouped into time series for that area and are published as a single dataset.
* Samples collected from 32 cutbanks along several km of Roberts Creek, northeast Iowa. Each sample is from a different site, but they form a time series from 0-12,510 14C yr BP, and pollen, plant macrofossils, and beetles were published and graphed as if from a single site.
* A set of pollen surface samples from a particular region or study that were published and analyzed as a single dataset and submitted to the database as a single dataset.
The examples above are datasets predefined in the database. New aggregate datasets could be assembled for particular studies, for example all the pollen samples for a given time slice for a given geographic region.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eaggregatedatasets-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/aggregatedatasets.html)

{{ table_structure("aggregatedatasets") }}

## Statistics

{{ table_stats("aggregatedatasets") }}

## Relationships

**Primary Key**: `aggregatedatasetid`

**Foreign Keys**:

- `aggregateordertypeid` → [`aggregateordertypes.aggregateordertypeid`](aggregateordertypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("aggregatedatasets") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from aggregatedatasets
SELECT *
FROM aggregatedatasets
ORDER BY aggregatedatasetid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from aggregatedatasets

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM aggregatedatasets;
```

**Purpose**: Get the total number of records in aggregatedatasets

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM aggregatedatasets
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from aggregatedatasets within a specific date range

### Example 4: Join with aggregateordertypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM aggregatedatasets t1
INNER JOIN aggregateordertypes t2 
    ON t1.aggregateordertypeid = t2.aggregateordertypeid
LIMIT 100;
```

**Purpose**: Retrieve aggregatedatasets records with related data from aggregateordertypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by aggregatedatasetname
SELECT 
    aggregatedatasetname,
    COUNT(*) as count
FROM aggregatedatasets
GROUP BY aggregatedatasetname
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by aggregatedatasetname

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
