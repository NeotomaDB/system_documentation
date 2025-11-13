---
title: Geopoliticalunits
description: Lookup table of GeoPoliticalUnits. Table is referenced by the SiteGeoPolitical table. These are coun
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.geopoliticalunits`

## Description

Lookup table of GeoPoliticalUnits. Table is referenced by the SiteGeoPolitical table. These are countries and various subdivisions. Countries and subdivisions were acquired from the U.S. Central Intelligence Agency World Factbook8 and the ISO 3166-1 and ISO 3166-2 databases9.
Each GeoPolitical Unit has a rank. GeoPolitical Units with Rank 1 are generally countries. There are a few exceptions, including Antarctica and island territories, such as Greenland, which although a Danish territory, is geographically separate and distinct. Rank 2 units are generally secondary political divisions with various designations: e.g. states in the United States, provinces in Canada, and regions in France. For some countries, the secondary divisions are not political but rather distinct geographic entities, such as islands. The secondary divisions of some island nations include either groups of islands or sections of more highly populated islands; however, the actual island on which a site is located is more important information. Some countries also have Rank 3 units, e.g. counties in the United States and metropolitan departments in France. In addition to purely political units, various other administrative regions and geographic entities can be contained in this table. Examples of administrative regions are National Parks and Forests. It might be quite useful, for example, to have a record of all the sites in Yellowstone National Park. These additional units are Rank 4, and they can be added to the database as warranted.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2egeopoliticalunits-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/geopoliticalunits.html)

{{ table_structure("geopoliticalunits") }}

## Statistics

{{ table_stats("geopoliticalunits") }}

## Relationships

**Primary Key**: `geopoliticalid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("geopoliticalunits") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from geopoliticalunits
SELECT *
FROM geopoliticalunits
ORDER BY geopoliticalid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from geopoliticalunits

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM geopoliticalunits;
```

**Purpose**: Get the total number of records in geopoliticalunits

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM geopoliticalunits
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from geopoliticalunits within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by geopoliticalname
SELECT 
    geopoliticalname,
    COUNT(*) as count
FROM geopoliticalunits
GROUP BY geopoliticalname
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by geopoliticalname

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
