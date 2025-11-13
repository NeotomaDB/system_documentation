---
title: Chroncontrolscal14C
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.chroncontrolscal14c`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2echroncontrolscal14c-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/chroncontrolscal14c.html)

{{ table_structure("chroncontrolscal14c") }}

## Statistics

{{ table_stats("chroncontrolscal14c") }}

## Relationships

**Primary Key**: `chroncontrolid`

**Foreign Keys**:

- `calibrationcurveid` → [`calibrationcurves.calibrationcurveid`](calibrationcurves.md)
- `calibrationprogramid` → [`calibrationprograms.calibrationprogramid`](calibrationprograms.md)
- `chroncontrolid` → [`chroncontrols.chroncontrolid`](chroncontrols.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("chroncontrolscal14c") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from chroncontrolscal14c
SELECT *
FROM chroncontrolscal14c
ORDER BY chroncontrolid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from chroncontrolscal14c

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM chroncontrolscal14c;
```

**Purpose**: Get the total number of records in chroncontrolscal14c

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM chroncontrolscal14c
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from chroncontrolscal14c within a specific date range

### Example 4: Join with calibrationcurves

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM chroncontrolscal14c t1
INNER JOIN calibrationcurves t2 
    ON t1.calibrationcurveid = t2.calibrationcurveid
LIMIT 100;
```

**Purpose**: Retrieve chroncontrolscal14c records with related data from calibrationcurves

### Example 5: Aggregate Data

```sql
-- Aggregate records by calibrationcurveid
SELECT 
    calibrationcurveid,
    COUNT(*) as count
FROM chroncontrolscal14c
GROUP BY calibrationcurveid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by calibrationcurveid

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
