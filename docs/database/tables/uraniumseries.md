---
title: Uraniumseries
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.uraniumseries`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2euraniumseries-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/uraniumseries.html)

{{ table_structure("uraniumseries") }}

## Statistics

{{ table_stats("uraniumseries") }}

## Relationships

**Foreign Keys**:

- `decayconstantid` → [`decayconstants.decayconstantid`](decayconstants.md)
- `geochronid` → [`geochronology.geochronid`](geochronology.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("uraniumseries") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from uraniumseries
SELECT *
FROM uraniumseries
ORDER BY geochronid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from uraniumseries

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM uraniumseries;
```

**Purpose**: Get the total number of records in uraniumseries

### Example 3: Join with decayconstants

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM uraniumseries t1
INNER JOIN decayconstants t2 
    ON t1.decayconstantid = t2.decayconstantid
LIMIT 100;
```

**Purpose**: Retrieve uraniumseries records with related data from decayconstants

### Example 4: Aggregate Data

```sql
-- Aggregate records by decayconstantid
SELECT 
    decayconstantid,
    COUNT(*) as count
FROM uraniumseries
GROUP BY decayconstantid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by decayconstantid

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
