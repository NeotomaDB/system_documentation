---
title: Hiatuses
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.hiatuses`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2ehiatuses-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/hiatuses.html)

{{ table_structure("hiatuses") }}

## Statistics

{{ table_stats("hiatuses") }}

## Relationships

**Primary Key**: `hiatusid`

**Foreign Keys**:

- `analysisunitend` → [`analysisunits.analysisunitid`](analysisunits.md)
- `analysisunitstart` → [`analysisunits.analysisunitid`](analysisunits.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("hiatuses") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from hiatuses
SELECT *
FROM hiatuses
ORDER BY hiatusid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from hiatuses

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM hiatuses;
```

**Purpose**: Get the total number of records in hiatuses

### Example 3: Join with analysisunits

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM hiatuses t1
INNER JOIN analysisunits t2 
    ON t1.analysisunitend = t2.analysisunitid
LIMIT 100;
```

**Purpose**: Retrieve hiatuses records with related data from analysisunits

### Example 4: Aggregate Data

```sql
-- Aggregate records by analysisunitstart
SELECT 
    analysisunitstart,
    COUNT(*) as count
FROM hiatuses
GROUP BY analysisunitstart
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by analysisunitstart

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
