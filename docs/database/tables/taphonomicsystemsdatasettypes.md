---
title: Taphonomicsystemsdatasettypes
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.taphonomicsystemsdatasettypes`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2etaphonomicsystemsdatasettypes-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/taphonomicsystemsdatasettypes.html)

{{ table_structure("taphonomicsystemsdatasettypes") }}

## Statistics

{{ table_stats("taphonomicsystemsdatasettypes") }}

## Relationships

**Primary Key**: `datasettypeid, taphonomicsystemid`

**Foreign Keys**:

- `taphonomicsystemid` → [`taphonomicsystems.taphonomicsystemid`](taphonomicsystems.md)
- `datasettypeid` → [`datasettypes.datasettypeid`](datasettypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("taphonomicsystemsdatasettypes") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from taphonomicsystemsdatasettypes
SELECT *
FROM taphonomicsystemsdatasettypes
ORDER BY datasettypeid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from taphonomicsystemsdatasettypes

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM taphonomicsystemsdatasettypes;
```

**Purpose**: Get the total number of records in taphonomicsystemsdatasettypes

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM taphonomicsystemsdatasettypes
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from taphonomicsystemsdatasettypes within a specific date range

### Example 4: Join with taphonomicsystems

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM taphonomicsystemsdatasettypes t1
INNER JOIN taphonomicsystems t2 
    ON t1.taphonomicsystemid = t2.taphonomicsystemid
LIMIT 100;
```

**Purpose**: Retrieve taphonomicsystemsdatasettypes records with related data from taphonomicsystems

### Example 5: Aggregate Data

```sql
-- Aggregate records by taphonomicsystemid
SELECT 
    taphonomicsystemid,
    COUNT(*) as count
FROM taphonomicsystemsdatasettypes
GROUP BY taphonomicsystemid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by taphonomicsystemid

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
