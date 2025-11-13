---
title: Entityvegetationcover
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.entityvegetationcover`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eentityvegetationcover-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/entityvegetationcover.html)

{{ table_structure("entityvegetationcover") }}

## Statistics

{{ table_stats("entityvegetationcover") }}

## Relationships

**Foreign Keys**:

- `entityid` → [`speleothems.entityid`](speleothems.md)
- `vegetationcovertypeid` → [`vegetationcovertypes.vegetationcovertypeid`](vegetationcovertypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("entityvegetationcover") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from entityvegetationcover
SELECT *
FROM entityvegetationcover
ORDER BY entityid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from entityvegetationcover

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM entityvegetationcover;
```

**Purpose**: Get the total number of records in entityvegetationcover

### Example 3: Join with speleothems

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM entityvegetationcover t1
INNER JOIN speleothems t2 
    ON t1.entityid = t2.entityid
LIMIT 100;
```

**Purpose**: Retrieve entityvegetationcover records with related data from speleothems

### Example 4: Aggregate Data

```sql
-- Aggregate records by vegetationcovertypeid
SELECT 
    vegetationcovertypeid,
    COUNT(*) as count
FROM entityvegetationcover
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
