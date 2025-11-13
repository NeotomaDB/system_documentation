---
title: Ecolgrouptypes
description: Lookup table of Ecological Group Types. Table is referenced by the EcolGroups table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.ecolgrouptypes`

## Description

Lookup table of Ecological Group Types. Table is referenced by the EcolGroups table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eecolgrouptypes-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/ecolgrouptypes.html)

{{ table_structure("ecolgrouptypes") }}

## Statistics

{{ table_stats("ecolgrouptypes") }}

## Relationships

**Primary Key**: `ecolgroupid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("ecolgrouptypes") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from ecolgrouptypes
SELECT *
FROM ecolgrouptypes
ORDER BY ecolgroupid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from ecolgrouptypes

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM ecolgrouptypes;
```

**Purpose**: Get the total number of records in ecolgrouptypes

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM ecolgrouptypes
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from ecolgrouptypes within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by ecolgroup
SELECT 
    ecolgroup,
    COUNT(*) as count
FROM ecolgrouptypes
GROUP BY ecolgroup
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by ecolgroup

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
