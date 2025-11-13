---
title: Geochronology
description: This table stores geochronologic data. Geochronologic measurements are from geochronologic samples, 
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.geochronology`

## Description

This table stores geochronologic data. Geochronologic measurements are from geochronologic samples, which are from Analysis Units, which may have a depth and thickness. Geochronologic measurements may be from the same or different Analysis Units as fossils. In the case of faunal excavations, geochronologic samples are typically from the same Analysis Units as the fossils, and there may be multiple geochronologic samples from a single Analysis Unit. In the case of cores used for microfossil analysis, geochronologic samples are often from separate Analysis Units; dated core sections are often thicker than microfossil Analysis Units.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2egeochronology-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/geochronology.html)

{{ table_structure("geochronology") }}

## Statistics

{{ table_stats("geochronology") }}

## Relationships

**Primary Key**: `geochronid`

**Foreign Keys**:

- `agetypeid` → [`agetypes.agetypeid`](agetypes.md)
- `geochrontypeid` → [`geochrontypes.geochrontypeid`](geochrontypes.md)
- `sampleid` → [`samples.sampleid`](samples.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("geochronology") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from geochronology
SELECT *
FROM geochronology
ORDER BY geochronid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from geochronology

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM geochronology;
```

**Purpose**: Get the total number of records in geochronology

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM geochronology
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from geochronology within a specific date range

### Example 4: Join with agetypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM geochronology t1
INNER JOIN agetypes t2 
    ON t1.agetypeid = t2.agetypeid
LIMIT 100;
```

**Purpose**: Retrieve geochronology records with related data from agetypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by sampleid
SELECT 
    sampleid,
    COUNT(*) as count
FROM geochronology
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
