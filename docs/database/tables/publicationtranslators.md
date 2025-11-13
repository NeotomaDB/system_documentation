---
title: Publicationtranslators
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.publicationtranslators`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2epublicationtranslators-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/publicationtranslators.html)

{{ table_structure("publicationtranslators") }}

## Statistics

{{ table_stats("publicationtranslators") }}

## Relationships

**Primary Key**: `translatorid`

**Foreign Keys**:

- `publicationid` → [`publications.publicationid`](publications.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("publicationtranslators") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from publicationtranslators
SELECT *
FROM publicationtranslators
ORDER BY translatorid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from publicationtranslators

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM publicationtranslators;
```

**Purpose**: Get the total number of records in publicationtranslators

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM publicationtranslators
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from publicationtranslators within a specific date range

### Example 4: Join with publications

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM publicationtranslators t1
INNER JOIN publications t2 
    ON t1.publicationid = t2.publicationid
LIMIT 100;
```

**Purpose**: Retrieve publicationtranslators records with related data from publications

### Example 5: Aggregate Data

```sql
-- Aggregate records by publicationid
SELECT 
    publicationid,
    COUNT(*) as count
FROM publicationtranslators
GROUP BY publicationid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by publicationid

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
