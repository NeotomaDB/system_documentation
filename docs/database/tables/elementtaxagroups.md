---
title: Elementtaxagroups
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.elementtaxagroups`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eelementtaxagroups-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/elementtaxagroups.html)

{{ table_structure("elementtaxagroups") }}

## Statistics

{{ table_stats("elementtaxagroups") }}

## Relationships

**Primary Key**: `elementtaxagroupid`

**Foreign Keys**:

- `elementtypeid` → [`elementtypes.elementtypeid`](elementtypes.md)
- `taxagroupid` → [`taxagrouptypes.taxagroupid`](taxagrouptypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("elementtaxagroups") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from elementtaxagroups
SELECT *
FROM elementtaxagroups
ORDER BY elementtaxagroupid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from elementtaxagroups

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM elementtaxagroups;
```

**Purpose**: Get the total number of records in elementtaxagroups

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM elementtaxagroups
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from elementtaxagroups within a specific date range

### Example 4: Join with elementtypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM elementtaxagroups t1
INNER JOIN elementtypes t2 
    ON t1.elementtypeid = t2.elementtypeid
LIMIT 100;
```

**Purpose**: Retrieve elementtaxagroups records with related data from elementtypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by taxagroupid
SELECT 
    taxagroupid,
    COUNT(*) as count
FROM elementtaxagroups
GROUP BY taxagroupid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by taxagroupid

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
