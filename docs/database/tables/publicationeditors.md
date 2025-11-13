---
title: Publicationeditors
description: This table stores the editors of publications for which chapters or sections are the primary bibliog
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.publicationeditors`

## Description

This table stores the editors of publications for which chapters or sections are the primary bibliographic entries. Chapter authors are stored in the PublicatonAuthors table, where they are linked to the Contacts table. However, publication editors are not cross-referenced in the Contacts table, because chapter authors are the principal citation.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2epublicationeditors-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/publicationeditors.html)

{{ table_structure("publicationeditors") }}

## Statistics

{{ table_stats("publicationeditors") }}

## Relationships

**Primary Key**: `editorid`

**Foreign Keys**:

- `publicationid` → [`publications.publicationid`](publications.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("publicationeditors") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from publicationeditors
SELECT *
FROM publicationeditors
ORDER BY editorid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from publicationeditors

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM publicationeditors;
```

**Purpose**: Get the total number of records in publicationeditors

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM publicationeditors
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from publicationeditors within a specific date range

### Example 4: Join with publications

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM publicationeditors t1
INNER JOIN publications t2 
    ON t1.publicationid = t2.publicationid
LIMIT 100;
```

**Purpose**: Retrieve publicationeditors records with related data from publications

### Example 5: Aggregate Data

```sql
-- Aggregate records by publicationid
SELECT 
    publicationid,
    COUNT(*) as count
FROM publicationeditors
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
