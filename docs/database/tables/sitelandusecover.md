---
title: Sitelandusecover
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.sitelandusecover`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esitelandusecover-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/sitelandusecover.html)

{{ table_structure("sitelandusecover") }}

## Statistics

{{ table_stats("sitelandusecover") }}

## Relationships

**Foreign Keys**:

- `landusecovertypeid` → [`vegetationcovertypes.vegetationcovertypeid`](vegetationcovertypes.md)
- `siteid` → [`sites.siteid`](sites.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("sitelandusecover") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from sitelandusecover
SELECT *
FROM sitelandusecover
ORDER BY siteid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from sitelandusecover

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM sitelandusecover;
```

**Purpose**: Get the total number of records in sitelandusecover

### Example 3: Join with vegetationcovertypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM sitelandusecover t1
INNER JOIN vegetationcovertypes t2 
    ON t1.landusecovertypeid = t2.vegetationcovertypeid
LIMIT 100;
```

**Purpose**: Retrieve sitelandusecover records with related data from vegetationcovertypes

### Example 4: Aggregate Data

```sql
-- Aggregate records by landusecovertypeid
SELECT 
    landusecovertypeid,
    COUNT(*) as count
FROM sitelandusecover
GROUP BY landusecovertypeid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by landusecovertypeid

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
