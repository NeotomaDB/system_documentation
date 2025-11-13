---
title: Entityrelationship
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.entityrelationship`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eentityrelationship-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/entityrelationship.html)

{{ table_structure("entityrelationship") }}

## Statistics

{{ table_stats("entityrelationship") }}

## Relationships

**Foreign Keys**:

- `entityid` → [`speleothems.entityid`](speleothems.md)
- `entitystatusid` → [`speleothementitystatuses.entitystatusid`](speleothementitystatuses.md)
- `referenceentityid` → [`speleothems.entityid`](speleothems.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("entityrelationship") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from entityrelationship
SELECT *
FROM entityrelationship
ORDER BY entityid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from entityrelationship

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM entityrelationship;
```

**Purpose**: Get the total number of records in entityrelationship

### Example 3: Join with speleothems

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM entityrelationship t1
INNER JOIN speleothems t2 
    ON t1.entityid = t2.entityid
LIMIT 100;
```

**Purpose**: Retrieve entityrelationship records with related data from speleothems

### Example 4: Aggregate Data

```sql
-- Aggregate records by entitystatusid
SELECT 
    entitystatusid,
    COUNT(*) as count
FROM entityrelationship
GROUP BY entitystatusid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by entitystatusid

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
