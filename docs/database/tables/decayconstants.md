---
title: Decayconstants
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.decayconstants`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2edecayconstants-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/decayconstants.html)

{{ table_structure("decayconstants") }}

## Statistics

{{ table_stats("decayconstants") }}

## Relationships

**Primary Key**: `decayconstantid`

**Foreign Keys**:

- `publicationid` → [`publications.publicationid`](publications.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("decayconstants") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from decayconstants
SELECT *
FROM decayconstants
ORDER BY decayconstantid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from decayconstants

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM decayconstants;
```

**Purpose**: Get the total number of records in decayconstants

### Example 3: Join with publications

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM decayconstants t1
INNER JOIN publications t2 
    ON t1.publicationid = t2.publicationid
LIMIT 100;
```

**Purpose**: Retrieve decayconstants records with related data from publications

### Example 4: Aggregate Data

```sql
-- Aggregate records by decayconstant
SELECT 
    decayconstant,
    COUNT(*) as count
FROM decayconstants
GROUP BY decayconstant
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by decayconstant

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
