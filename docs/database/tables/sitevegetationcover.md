---
title: Sitevegetationcover
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.sitevegetationcover`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esitevegetationcover-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/sitevegetationcover.html)

{{ table_structure("sitevegetationcover") }}

## Statistics

{{ table_stats("sitevegetationcover") }}

## Relationships

**Foreign Keys**:

- `siteid` → [`sites.siteid`](sites.md)
- `vegetationcovertypeid` → [`vegetationcovertypes.vegetationcovertypeid`](vegetationcovertypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("sitevegetationcover") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from sitevegetationcover
SELECT *
FROM sitevegetationcover
ORDER BY siteid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from sitevegetationcover

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM sitevegetationcover;
```

**Purpose**: Get the total number of records in sitevegetationcover

### Example 3: Join with sites

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM sitevegetationcover t1
INNER JOIN sites t2 
    ON t1.siteid = t2.siteid
LIMIT 100;
```

**Purpose**: Retrieve sitevegetationcover records with related data from sites

### Example 4: Aggregate Data

```sql
-- Aggregate records by vegetationcovertypeid
SELECT 
    vegetationcovertypeid,
    COUNT(*) as count
FROM sitevegetationcover
GROUP BY vegetationcovertypeid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by vegetationcovertypeid

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
