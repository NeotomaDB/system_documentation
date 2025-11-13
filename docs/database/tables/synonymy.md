---
title: Synonymy
description: The synonymy table links dataset-level synonymies to particular publications or contacts.  This allo
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.synonymy`

## Description

The synonymy table links dataset-level synonymies to particular publications or contacts.  This allows users to maintain the original taxonomic information within a table, but tie it to newer and more authoritative taxonomic information.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esynonymy-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/synonymy.html)

{{ table_structure("synonymy") }}

## Statistics

{{ table_stats("synonymy") }}

## Relationships

**Primary Key**: `synonymyid`

**Foreign Keys**:

- `contactid` → [`contacts.contactid`](contacts.md)
- `datasetid` → [`datasets.datasetid`](datasets.md)
- `publicationid` → [`publications.publicationid`](publications.md)
- `taxonid` → [`taxa.taxonid`](taxa.md)
- `reftaxonid` → [`taxa.taxonid`](taxa.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("synonymy") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from synonymy
SELECT *
FROM synonymy
ORDER BY synonymyid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from synonymy

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM synonymy;
```

**Purpose**: Get the total number of records in synonymy

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM synonymy
WHERE datesynonymized >= '2024-01-01'
  AND datesynonymized < '2025-01-01'
ORDER BY datesynonymized DESC;
```

**Purpose**: Retrieve records from synonymy within a specific date range

### Example 4: Join with contacts

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM synonymy t1
INNER JOIN contacts t2 
    ON t1.contactid = t2.contactid
LIMIT 100;
```

**Purpose**: Retrieve synonymy records with related data from contacts

### Example 5: Aggregate Data

```sql
-- Aggregate records by datasetid
SELECT 
    datasetid,
    COUNT(*) as count
FROM synonymy
GROUP BY datasetid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by datasetid

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
