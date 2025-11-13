---
title: Variables
description: This table lists Variables, which always consist of a Taxon and Units of measurement. Variables can 
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.variables`

## Description

This table lists Variables, which always consist of a Taxon and Units of measurement. Variables can also have Elements, Contexts, and Modifications. Thus, the same taxon with different measurement units (e.g. present/absent, NISP, MNI) are different Variables.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2evariables-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/variables.html)

{{ table_structure("variables") }}

## Statistics

{{ table_stats("variables") }}

## Relationships

**Primary Key**: `variableid`

**Foreign Keys**:

- `taxonid` → [`taxa.taxonid`](taxa.md)
- `variablecontextid` → [`variablecontexts.variablecontextid`](variablecontexts.md)
- `variableelementid` → [`variableelements.variableelementid`](variableelements.md)
- `variableunitsid` → [`variableunits.variableunitsid`](variableunits.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("variables") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from variables
SELECT *
FROM variables
ORDER BY variableid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from variables

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM variables;
```

**Purpose**: Get the total number of records in variables

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM variables
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from variables within a specific date range

### Example 4: Join with taxa

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM variables t1
INNER JOIN taxa t2 
    ON t1.taxonid = t2.taxonid
LIMIT 100;
```

**Purpose**: Retrieve variables records with related data from taxa

### Example 5: Aggregate Data

```sql
-- Aggregate records by taxonid
SELECT 
    taxonid,
    COUNT(*) as count
FROM variables
GROUP BY taxonid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by taxonid

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
