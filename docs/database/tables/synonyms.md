---
title: Synonyms
description: This table lists common synonyms for taxa in the Taxa table. No effort has been made to provide a co
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.synonyms`

## Description

This table lists common synonyms for taxa in the Taxa table. No effort has been made to provide a complete taxonomic synonymy, but rather to list synonyms commonly used in recent literature.  This table is not the same as the Synonomy table, also present in Neotoma, which links a specific synonymy to a dataset

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esynonyms-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/synonyms.html)

{{ table_structure("synonyms") }}

## Statistics

{{ table_stats("synonyms") }}

## Relationships

**Primary Key**: `synonymid`

**Foreign Keys**:

- `invalidtaxonid` → [`taxa.taxonid`](taxa.md)
- `synonymtypeid` → [`synonymtypes.synonymtypeid`](synonymtypes.md)
- `validtaxonid` → [`taxa.taxonid`](taxa.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("synonyms") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from synonyms
SELECT *
FROM synonyms
ORDER BY synonymid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from synonyms

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM synonyms;
```

**Purpose**: Get the total number of records in synonyms

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM synonyms
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from synonyms within a specific date range

### Example 4: Join with taxa

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM synonyms t1
INNER JOIN taxa t2 
    ON t1.invalidtaxonid = t2.taxonid
LIMIT 100;
```

**Purpose**: Retrieve synonyms records with related data from taxa

### Example 5: Aggregate Data

```sql
-- Aggregate records by invalidtaxonid
SELECT 
    invalidtaxonid,
    COUNT(*) as count
FROM synonyms
GROUP BY invalidtaxonid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by invalidtaxonid

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
