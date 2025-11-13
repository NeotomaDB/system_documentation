---
title: Summarydatataphonomy
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.summarydatataphonomy`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esummarydatataphonomy-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/summarydatataphonomy.html)

{{ table_structure("summarydatataphonomy") }}

## Statistics

{{ table_stats("summarydatataphonomy") }}

## Relationships

**Primary Key**: `dataid, taphonomictypeid`

**Foreign Keys**:

- `dataid` → [`data.dataid`](data.md)
- `taphonomictypeid` → [`taphonomictypes.taphonomictypeid`](taphonomictypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("summarydatataphonomy") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from summarydatataphonomy
SELECT *
FROM summarydatataphonomy
ORDER BY dataid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from summarydatataphonomy

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM summarydatataphonomy;
```

**Purpose**: Get the total number of records in summarydatataphonomy

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM summarydatataphonomy
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from summarydatataphonomy within a specific date range

### Example 4: Join with data

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM summarydatataphonomy t1
INNER JOIN data t2 
    ON t1.dataid = t2.dataid
LIMIT 100;
```

**Purpose**: Retrieve summarydatataphonomy records with related data from data

### Example 5: Aggregate Data

```sql
-- Aggregate records by taphonomictypeid
SELECT 
    taphonomictypeid,
    COUNT(*) as count
FROM summarydatataphonomy
GROUP BY taphonomictypeid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by taphonomictypeid

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
