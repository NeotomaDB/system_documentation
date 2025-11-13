---
title: Speleothemcollectionunits
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.speleothemcollectionunits`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2espeleothemcollectionunits-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/speleothemcollectionunits.html)

{{ table_structure("speleothemcollectionunits") }}

## Statistics

{{ table_stats("speleothemcollectionunits") }}

## Relationships

**Foreign Keys**:

- `collectionunitid` → [`collectionunits.collectionunitid`](collectionunits.md)
- `entityid` → [`speleothems.entityid`](speleothems.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("speleothemcollectionunits") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from speleothemcollectionunits
SELECT *
FROM speleothemcollectionunits
ORDER BY entityid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from speleothemcollectionunits

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM speleothemcollectionunits;
```

**Purpose**: Get the total number of records in speleothemcollectionunits

### Example 3: Join with collectionunits

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM speleothemcollectionunits t1
INNER JOIN collectionunits t2 
    ON t1.collectionunitid = t2.collectionunitid
LIMIT 100;
```

**Purpose**: Retrieve speleothemcollectionunits records with related data from collectionunits

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
