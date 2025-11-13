---
title: Taxa
description: This table lists all taxa in the database. Most taxa are biological taxa; however, some are biometri
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.taxa`

## Description

This table lists all taxa in the database. Most taxa are biological taxa; however, some are biometric measures and some are physical parameters.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2etaxa-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/taxa.html)

{{ table_structure("taxa") }}

## Statistics

{{ table_stats("taxa") }}

## Relationships

**Primary Key**: `taxonid`

**Foreign Keys**:

- `highertaxonid` → [`taxa.taxonid`](taxa.md)
- `publicationid` → [`publications.publicationid`](publications.md)
- `taxagroupid` → [`taxagrouptypes.taxagroupid`](taxagrouptypes.md)
- `validatorid` → [`contacts.contactid`](contacts.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("taxa") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from taxa
SELECT *
FROM taxa
ORDER BY taxonid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from taxa

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM taxa;
```

**Purpose**: Get the total number of records in taxa

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM taxa
WHERE validatedate >= '2024-01-01'
  AND validatedate < '2025-01-01'
ORDER BY validatedate DESC;
```

**Purpose**: Retrieve records from taxa within a specific date range

### Example 4: Join with taxa

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM taxa t1
INNER JOIN taxa t2 
    ON t1.highertaxonid = t2.taxonid
LIMIT 100;
```

**Purpose**: Retrieve taxa records with related data from taxa

### Example 5: Aggregate Data

```sql
-- Aggregate records by taxoncode
SELECT 
    taxoncode,
    COUNT(*) as count
FROM taxa
GROUP BY taxoncode
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by taxoncode

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
