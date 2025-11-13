---
title: Variableelements
description: Lookup table of Variable Elements. Table is referenced by the Variables table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.variableelements`

## Description

Lookup table of Variable Elements. Table is referenced by the Variables table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2evariableelements-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/variableelements.html)

{{ table_structure("variableelements") }}

## Statistics

{{ table_stats("variableelements") }}

## Relationships

**Primary Key**: `variableelementid`

**Foreign Keys**:

- `maturityid` → [`elementmaturities.maturityid`](elementmaturities.md)
- `portionid` → [`elementportions.portionid`](elementportions.md)
- `symmetryid` → [`elementsymmetries.symmetryid`](elementsymmetries.md)
- `elementtypeid` → [`elementtypes.elementtypeid`](elementtypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("variableelements") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from variableelements
SELECT *
FROM variableelements
ORDER BY variableelementid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from variableelements

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM variableelements;
```

**Purpose**: Get the total number of records in variableelements

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM variableelements
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from variableelements within a specific date range

### Example 4: Join with elementmaturities

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM variableelements t1
INNER JOIN elementmaturities t2 
    ON t1.maturityid = t2.maturityid
LIMIT 100;
```

**Purpose**: Retrieve variableelements records with related data from elementmaturities

### Example 5: Aggregate Data

```sql
-- Aggregate records by variableelement
SELECT 
    variableelement,
    COUNT(*) as count
FROM variableelements
GROUP BY variableelement
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by variableelement

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
