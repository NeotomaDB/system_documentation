---
title: Sampleages
description: This table stores sample ages. Ages are assigned to a Chronology. Because there may be more than one
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.sampleages`

## Description

This table stores sample ages. Ages are assigned to a Chronology. Because there may be more than one Chronology for a Collection Unit, samples may be assigned different ages for different Chronologies. A simple example is one sample age in radiocarbon years and another in calibrated radiocarbon years. The age units are an attribute of the Chronology.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esampleages-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/sampleages.html)

{{ table_structure("sampleages") }}

## Statistics

{{ table_stats("sampleages") }}

## Relationships

**Primary Key**: `sampleageid`

**Foreign Keys**:

- `chronologyid` → [`chronologies.chronologyid`](chronologies.md)
- `sampleid` → [`samples.sampleid`](samples.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("sampleages") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from sampleages
SELECT *
FROM sampleages
ORDER BY sampleageid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from sampleages

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM sampleages;
```

**Purpose**: Get the total number of records in sampleages

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM sampleages
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from sampleages within a specific date range

### Example 4: Join with chronologies

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM sampleages t1
INNER JOIN chronologies t2 
    ON t1.chronologyid = t2.chronologyid
LIMIT 100;
```

**Purpose**: Retrieve sampleages records with related data from chronologies

### Example 5: Aggregate Data

```sql
-- Aggregate records by sampleid
SELECT 
    sampleid,
    COUNT(*) as count
FROM sampleages
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
