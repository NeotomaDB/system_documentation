---
title: Geochronpublications
description: Publications in which Geochronologic measurements are reported. Many older radiocarbon dates are rep
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.geochronpublications`

## Description

Publications in which Geochronologic measurements are reported. Many older radiocarbon dates are reported in the journal Radiocarbon. Dates may be reported in multiple publications. The “publication” could be a database such as the online Canadian Archaeological Radiocarbon Database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2egeochronpublications-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/geochronpublications.html)

{{ table_structure("geochronpublications") }}

## Statistics

{{ table_stats("geochronpublications") }}

## Relationships

**Primary Key**: `geochronid, publicationid`

**Foreign Keys**:

- `geochronid` → [`geochronology.geochronid`](geochronology.md)
- `publicationid` → [`publications.publicationid`](publications.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("geochronpublications") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from geochronpublications
SELECT *
FROM geochronpublications
ORDER BY geochronid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from geochronpublications

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM geochronpublications;
```

**Purpose**: Get the total number of records in geochronpublications

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM geochronpublications
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from geochronpublications within a specific date range

### Example 4: Join with geochronology

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM geochronpublications t1
INNER JOIN geochronology t2 
    ON t1.geochronid = t2.geochronid
LIMIT 100;
```

**Purpose**: Retrieve geochronpublications records with related data from geochronology

### Example 5: Aggregate Data

```sql
-- Aggregate records by publicationid
SELECT 
    publicationid,
    COUNT(*) as count
FROM geochronpublications
GROUP BY publicationid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by publicationid

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
