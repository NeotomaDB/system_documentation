---
title: Formtaxa
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.formtaxa`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eformtaxa-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/formtaxa.html)

{{ table_structure("formtaxa") }}

## Statistics

{{ table_stats("formtaxa") }}

## Relationships

**Primary Key**: `formtaxonid`

**Foreign Keys**:

- `publicationid` → [`publications.publicationid`](publications.md)
- `taxonid` → [`taxa.taxonid`](taxa.md)
- `affinityid` → [`taxa.taxonid`](taxa.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("formtaxa") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from formtaxa
SELECT *
FROM formtaxa
ORDER BY formtaxonid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from formtaxa

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM formtaxa;
```

**Purpose**: Get the total number of records in formtaxa

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM formtaxa
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from formtaxa within a specific date range

### Example 4: Join with publications

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM formtaxa t1
INNER JOIN publications t2 
    ON t1.publicationid = t2.publicationid
LIMIT 100;
```

**Purpose**: Retrieve formtaxa records with related data from publications

### Example 5: Aggregate Data

```sql
-- Aggregate records by taxonid
SELECT 
    taxonid,
    COUNT(*) as count
FROM formtaxa
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
