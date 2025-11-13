---
title: Sites
description: The Sites table stores information about sites or localities, including name, geographic coordinates
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.sites`

## Description

The Sites table stores information about sites or localities, including name, geographic coordinates, and description. Sites generally have an areal extent and can be circumscribed by a latitude-longitude box. However, site data ingested from legacy databases have included only point locations. The lat-long box can be used either to circumscribe the aerial extent of a site or to provide purposeful imprecision to the site location. Site location may be imprecise because the original description was vague, e.g. «a gravel bar 5 miles east of town», or because the investigators, land owner, or land management agency may not want the exact location made public, perhaps to prevent looting and vandalism. In the first case, the lat-long box can be made sufficiently large to encompass the true location and in the second case to prevent exact location.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esites-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/sites.html)

{{ table_structure("sites") }}

## Statistics

{{ table_stats("sites") }}

## Relationships

**Primary Key**: `siteid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("sites") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from sites
SELECT *
FROM sites
ORDER BY siteid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from sites

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM sites;
```

**Purpose**: Get the total number of records in sites

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM sites
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from sites within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by sitename
SELECT 
    sitename,
    COUNT(*) as count
FROM sites
GROUP BY sitename
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by sitename

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
