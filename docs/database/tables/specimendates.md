---
title: Specimendates
description: This table enables queries for dated specimens of individual taxa. Although the MaterialDated field 
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.specimendates`

## Description

This table enables queries for dated specimens of individual taxa. Although the MaterialDated field in the Geochronology table may list the taxa dated, this protocol is not enforced, and the field is not linked to the taxa table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2especimendates-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/specimendates.html)

{{ table_structure("specimendates") }}

## Statistics

{{ table_stats("specimendates") }}

## Relationships

**Primary Key**: `specimendateid`

**Foreign Keys**:

- `specimenid` → [`specimens.specimenid`](specimens.md)
- `elementtypeid` → [`elementtypes.elementtypeid`](elementtypes.md)
- `fractionid` → [`fractiondated.fractionid`](fractiondated.md)
- `geochronid` → [`geochronology.geochronid`](geochronology.md)
- `sampleid` → [`samples.sampleid`](samples.md)
- `taxonid` → [`taxa.taxonid`](taxa.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("specimendates") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from specimendates
SELECT *
FROM specimendates
ORDER BY specimendateid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from specimendates

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM specimendates;
```

**Purpose**: Get the total number of records in specimendates

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM specimendates
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from specimendates within a specific date range

### Example 4: Join with specimens

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM specimendates t1
INNER JOIN specimens t2 
    ON t1.specimenid = t2.specimenid
LIMIT 100;
```

**Purpose**: Retrieve specimendates records with related data from specimens

### Example 5: Aggregate Data

```sql
-- Aggregate records by geochronid
SELECT 
    geochronid,
    COUNT(*) as count
FROM specimendates
GROUP BY geochronid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by geochronid

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
