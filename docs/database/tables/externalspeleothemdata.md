---
title: Externalspeleothemdata
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.externalspeleothemdata`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eexternalspeleothemdata-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/externalspeleothemdata.html)

{{ table_structure("externalspeleothemdata") }}

## Statistics

{{ table_stats("externalspeleothemdata") }}

## Relationships

**Foreign Keys**:

- `entityid` → [`speleothems.entityid`](speleothems.md)
- `entityid` → [`speleothems.entityid`](speleothems.md)
- `extdatabaseid` → [`externaldatabases.extdatabaseid`](externaldatabases.md)
- `extdatabaseid` → [`externaldatabases.extdatabaseid`](externaldatabases.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("externalspeleothemdata") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from externalspeleothemdata
SELECT *
FROM externalspeleothemdata
ORDER BY entityid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from externalspeleothemdata

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM externalspeleothemdata;
```

**Purpose**: Get the total number of records in externalspeleothemdata

### Example 3: Join with speleothems

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM externalspeleothemdata t1
INNER JOIN speleothems t2 
    ON t1.entityid = t2.entityid
LIMIT 100;
```

**Purpose**: Retrieve externalspeleothemdata records with related data from speleothems

### Example 4: Aggregate Data

```sql
-- Aggregate records by externalid
SELECT 
    externalid,
    COUNT(*) as count
FROM externalspeleothemdata
GROUP BY externalid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by externalid

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
