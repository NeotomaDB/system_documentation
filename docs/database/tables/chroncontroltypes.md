---
title: Chroncontroltypes
description: Lookup table of Chronology Control Types. This table is referenced by the ChronControls table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.chroncontroltypes`

## Description

Lookup table of Chronology Control Types. This table is referenced by the ChronControls table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2echroncontroltypes-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/chroncontroltypes.html)

{{ table_structure("chroncontroltypes") }}

## Statistics

{{ table_stats("chroncontroltypes") }}

## Relationships

**Primary Key**: `chroncontroltypeid`

**Foreign Keys**:

- `higherchroncontroltypeid` → [`chroncontroltypes.chroncontroltypeid`](chroncontroltypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("chroncontroltypes") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from chroncontroltypes
SELECT *
FROM chroncontroltypes
ORDER BY chroncontroltypeid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from chroncontroltypes

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM chroncontroltypes;
```

**Purpose**: Get the total number of records in chroncontroltypes

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM chroncontroltypes
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from chroncontroltypes within a specific date range

### Example 4: Join with chroncontroltypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM chroncontroltypes t1
INNER JOIN chroncontroltypes t2 
    ON t1.higherchroncontroltypeid = t2.chroncontroltypeid
LIMIT 100;
```

**Purpose**: Retrieve chroncontroltypes records with related data from chroncontroltypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by chroncontroltype
SELECT 
    chroncontroltype,
    COUNT(*) as count
FROM chroncontroltypes
GROUP BY chroncontroltype
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by chroncontroltype

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
