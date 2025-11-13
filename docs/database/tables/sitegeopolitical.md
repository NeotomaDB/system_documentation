---
title: Sitegeopolitical
description: This table lists the GeoPolitical units in which sites occur.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.sitegeopolitical`

## Description

This table lists the GeoPolitical units in which sites occur.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esitegeopolitical-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/sitegeopolitical.html)

{{ table_structure("sitegeopolitical") }}

## Statistics

{{ table_stats("sitegeopolitical") }}

## Relationships

**Primary Key**: `sitegeopoliticalid`

**Foreign Keys**:

- `geopoliticalid` → [`geopoliticalunits.geopoliticalid`](geopoliticalunits.md)
- `siteid` → [`sites.siteid`](sites.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("sitegeopolitical") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from sitegeopolitical
SELECT *
FROM sitegeopolitical
ORDER BY sitegeopoliticalid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from sitegeopolitical

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM sitegeopolitical;
```

**Purpose**: Get the total number of records in sitegeopolitical

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM sitegeopolitical
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from sitegeopolitical within a specific date range

### Example 4: Join with geopoliticalunits

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM sitegeopolitical t1
INNER JOIN geopoliticalunits t2 
    ON t1.geopoliticalid = t2.geopoliticalid
LIMIT 100;
```

**Purpose**: Retrieve sitegeopolitical records with related data from geopoliticalunits

### Example 5: Aggregate Data

```sql
-- Aggregate records by siteid
SELECT 
    siteid,
    COUNT(*) as count
FROM sitegeopolitical
GROUP BY siteid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by siteid

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
