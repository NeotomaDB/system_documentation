---
title: Tephras
description: Tephras lookup table. This table stores recognized tephras with established ages. Referenced by the 
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.tephras`

## Description

Tephras lookup table. This table stores recognized tephras with established ages. Referenced by the Tephrachronology table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2etephras-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/tephras.html)

{{ table_structure("tephras") }}

## Statistics

{{ table_stats("tephras") }}

## Relationships

**Primary Key**: `tephraid`

**Foreign Keys**:

- `analysisunitid` → [`analysisunits.analysisunitid`](analysisunits.md)
- `eventid` → [`events.eventid`](events.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("tephras") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from tephras
SELECT *
FROM tephras
ORDER BY tephraid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from tephras

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM tephras;
```

**Purpose**: Get the total number of records in tephras

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM tephras
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from tephras within a specific date range

### Example 4: Join with analysisunits

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM tephras t1
INNER JOIN analysisunits t2 
    ON t1.analysisunitid = t2.analysisunitid
LIMIT 100;
```

**Purpose**: Retrieve tephras records with related data from analysisunits

### Example 5: Aggregate Data

```sql
-- Aggregate records by eventid
SELECT 
    eventid,
    COUNT(*) as count
FROM tephras
GROUP BY eventid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by eventid

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
