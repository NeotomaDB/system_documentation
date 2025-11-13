---
title: Relativeageunits
description: Lookup table of RelativeAgeUnits. Table is referenced by the RelativeAges table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.relativeageunits`

## Description

Lookup table of RelativeAgeUnits. Table is referenced by the RelativeAges table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2erelativeageunits-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/relativeageunits.html)

{{ table_structure("relativeageunits") }}

## Statistics

{{ table_stats("relativeageunits") }}

## Relationships

**Primary Key**: `relativeageunitid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("relativeageunits") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from relativeageunits
SELECT *
FROM relativeageunits
ORDER BY relativeageunitid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from relativeageunits

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM relativeageunits;
```

**Purpose**: Get the total number of records in relativeageunits

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM relativeageunits
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from relativeageunits within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by relativeageunit
SELECT 
    relativeageunit,
    COUNT(*) as count
FROM relativeageunits
GROUP BY relativeageunit
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by relativeageunit

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
