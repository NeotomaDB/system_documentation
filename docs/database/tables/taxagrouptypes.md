---
title: Taxagrouptypes
description: Lookup table for Taxa Group Types. This table is referenced by the Taxa table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.taxagrouptypes`

## Description

Lookup table for Taxa Group Types. This table is referenced by the Taxa table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2etaxagrouptypes-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/taxagrouptypes.html)

{{ table_structure("taxagrouptypes") }}

## Statistics

{{ table_stats("taxagrouptypes") }}

## Relationships

**Primary Key**: `taxagroupid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("taxagrouptypes") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from taxagrouptypes
SELECT *
FROM taxagrouptypes
ORDER BY taxagroupid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from taxagrouptypes

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM taxagrouptypes;
```

**Purpose**: Get the total number of records in taxagrouptypes

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM taxagrouptypes
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from taxagrouptypes within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by taxagroup
SELECT 
    taxagroup,
    COUNT(*) as count
FROM taxagrouptypes
GROUP BY taxagroup
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by taxagroup

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
