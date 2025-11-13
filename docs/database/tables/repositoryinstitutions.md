---
title: Repositoryinstitutions
description: A lookup table of institutions that are repositories for fossil specimens. Table is referenced by th
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.repositoryinstitutions`

## Description

A lookup table of institutions that are repositories for fossil specimens. Table is referenced by the RepositorySpecimens table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2erepositoryinstitutions-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/repositoryinstitutions.html)

{{ table_structure("repositoryinstitutions") }}

## Statistics

{{ table_stats("repositoryinstitutions") }}

## Relationships

**Primary Key**: `repositoryid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("repositoryinstitutions") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from repositoryinstitutions
SELECT *
FROM repositoryinstitutions
ORDER BY repositoryid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from repositoryinstitutions

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM repositoryinstitutions;
```

**Purpose**: Get the total number of records in repositoryinstitutions

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM repositoryinstitutions
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from repositoryinstitutions within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by acronym
SELECT 
    acronym,
    COUNT(*) as count
FROM repositoryinstitutions
GROUP BY acronym
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by acronym

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
