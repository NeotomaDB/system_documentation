---
title: Relativechronology
description: This table stores relative chronologic data. Relative Ages are assigned to Analysis Units, The Relat
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.relativechronology`

## Description

This table stores relative chronologic data. Relative Ages are assigned to Analysis Units, The Relative Age data along with any possible Geochronology and Tephrachronology data are used to create a chronology.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2erelativechronology-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/relativechronology.html)

{{ table_structure("relativechronology") }}

## Statistics

{{ table_stats("relativechronology") }}

## Relationships

**Primary Key**: `relativechronid`

**Foreign Keys**:

- `analysisunitid` → [`analysisunits.analysisunitid`](analysisunits.md)
- `relativeageid` → [`relativeages.relativeageid`](relativeages.md)
- `chroncontrolid` → [`chroncontrols.chroncontrolid`](chroncontrols.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("relativechronology") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from relativechronology
SELECT *
FROM relativechronology
ORDER BY relativechronid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from relativechronology

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM relativechronology;
```

**Purpose**: Get the total number of records in relativechronology

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM relativechronology
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from relativechronology within a specific date range

### Example 4: Join with analysisunits

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM relativechronology t1
INNER JOIN analysisunits t2 
    ON t1.analysisunitid = t2.analysisunitid
LIMIT 100;
```

**Purpose**: Retrieve relativechronology records with related data from analysisunits

### Example 5: Aggregate Data

```sql
-- Aggregate records by analysisunitid
SELECT 
    analysisunitid,
    COUNT(*) as count
FROM relativechronology
GROUP BY analysisunitid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by analysisunitid

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
