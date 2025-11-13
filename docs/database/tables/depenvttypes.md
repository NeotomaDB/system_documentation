---
title: Depenvttypes
description: Lookup table of Depositional Environment Types. Table is referenced by the CollectionUnits table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.depenvttypes`

## Description

Lookup table of Depositional Environment Types. Table is referenced by the CollectionUnits table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2edepenvttypes-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/depenvttypes.html)

{{ table_structure("depenvttypes") }}

## Statistics

{{ table_stats("depenvttypes") }}

## Relationships

**Primary Key**: `depenvtid`

**Foreign Keys**:

- `depenvthigherid` → [`depenvttypes.depenvtid`](depenvttypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("depenvttypes") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from depenvttypes
SELECT *
FROM depenvttypes
ORDER BY depenvtid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from depenvttypes

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM depenvttypes;
```

**Purpose**: Get the total number of records in depenvttypes

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM depenvttypes
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from depenvttypes within a specific date range

### Example 4: Join with depenvttypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM depenvttypes t1
INNER JOIN depenvttypes t2 
    ON t1.depenvthigherid = t2.depenvtid
LIMIT 100;
```

**Purpose**: Retrieve depenvttypes records with related data from depenvttypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by depenvt
SELECT 
    depenvt,
    COUNT(*) as count
FROM depenvttypes
GROUP BY depenvt
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by depenvt

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
