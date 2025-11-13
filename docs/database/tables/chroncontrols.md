---
title: Chroncontrols
description: This table stores data for Chronology Controls, which are the age-depth control points used for age 
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.chroncontrols`

## Description

This table stores data for Chronology Controls, which are the age-depth control points used for age models. These controls may be geophysical controls, such as radiocarbon dates, but include many other kinds of age controls, such as biostratigraphic controls, archaeological cultural associations, and volcanic tephras. In the case of radiocarbon dates, a Chronology Control may not simply be the raw radiocarbon date reported by the laboratory, but perhaps a radiocarbon date corrected for an old carbon reservoir, a calibrated radiocarbon date, or an average of several radiocarbon dates from the same level. A common control for lake-sediment cores is the age of the top of the core, which may be the year the core was taken or perhaps an estimate of 0 BP if a few cm of surficial sediment were lost.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2echroncontrols-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/chroncontrols.html)

{{ table_structure("chroncontrols") }}

## Statistics

{{ table_stats("chroncontrols") }}

## Relationships

**Primary Key**: `chroncontrolid`

**Foreign Keys**:

- `agetypeid` → [`agetypes.agetypeid`](agetypes.md)
- `analysisunitid` → [`analysisunits.analysisunitid`](analysisunits.md)
- `chroncontroltypeid` → [`chroncontroltypes.chroncontroltypeid`](chroncontroltypes.md)
- `chronologyid` → [`chronologies.chronologyid`](chronologies.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("chroncontrols") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from chroncontrols
SELECT *
FROM chroncontrols
ORDER BY chroncontrolid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from chroncontrols

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM chroncontrols;
```

**Purpose**: Get the total number of records in chroncontrols

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM chroncontrols
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from chroncontrols within a specific date range

### Example 4: Join with agetypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM chroncontrols t1
INNER JOIN agetypes t2 
    ON t1.agetypeid = t2.agetypeid
LIMIT 100;
```

**Purpose**: Retrieve chroncontrols records with related data from agetypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by chronologyid
SELECT 
    chronologyid,
    COUNT(*) as count
FROM chroncontrols
GROUP BY chronologyid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by chronologyid

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
