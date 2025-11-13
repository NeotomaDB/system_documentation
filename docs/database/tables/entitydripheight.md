---
title: Entitydripheight
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.entitydripheight`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eentitydripheight-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/entitydripheight.html)

{{ table_structure("entitydripheight") }}

## Statistics

{{ table_stats("entitydripheight") }}

## Relationships

**Foreign Keys**:

- `entitydripheightunit` → [`variableunits.variableunitsid`](variableunits.md)
- `entityid` → [`speleothems.entityid`](speleothems.md)
- `speleothemdriptypeid` → [`speleothemdriptypes.speleothemdriptypeid`](speleothemdriptypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("entitydripheight") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from entitydripheight
SELECT *
FROM entitydripheight
ORDER BY entityid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from entitydripheight

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM entitydripheight;
```

**Purpose**: Get the total number of records in entitydripheight

### Example 3: Join with variableunits

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM entitydripheight t1
INNER JOIN variableunits t2 
    ON t1.entitydripheightunit = t2.variableunitsid
LIMIT 100;
```

**Purpose**: Retrieve entitydripheight records with related data from variableunits

### Example 4: Aggregate Data

```sql
-- Aggregate records by speleothemdriptypeid
SELECT 
    speleothemdriptypeid,
    COUNT(*) as count
FROM entitydripheight
GROUP BY speleothemdriptypeid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by speleothemdriptypeid

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
