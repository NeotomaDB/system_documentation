---
title: Isostratdata
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.isostratdata`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eisostratdata-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/isostratdata.html)

{{ table_structure("isostratdata") }}

## Statistics

{{ table_stats("isostratdata") }}

## Relationships

**Primary Key**: `dataid`

**Foreign Keys**:

- `dataid` → [`data.dataid`](data.md)
- `elementtypeid` → [`elementtypes.elementtypeid`](elementtypes.md)
- `taxonid` → [`taxa.taxonid`](taxa.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("isostratdata") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from isostratdata
SELECT *
FROM isostratdata
ORDER BY dataid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from isostratdata

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM isostratdata;
```

**Purpose**: Get the total number of records in isostratdata

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM isostratdata
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from isostratdata within a specific date range

### Example 4: Join with data

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM isostratdata t1
INNER JOIN data t2 
    ON t1.dataid = t2.dataid
LIMIT 100;
```

**Purpose**: Retrieve isostratdata records with related data from data

### Example 5: Aggregate Data

```sql
-- Aggregate records by sd
SELECT 
    sd,
    COUNT(*) as count
FROM isostratdata
GROUP BY sd
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by sd

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
