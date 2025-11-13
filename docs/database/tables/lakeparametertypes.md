---
title: Lakeparametertypes
description: A set of variables associated with lakes, including area, depth and volume.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.lakeparametertypes`

## Description

A set of variables associated with lakes, including area, depth and volume.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2elakeparametertypes-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/lakeparametertypes.html)

{{ table_structure("lakeparametertypes") }}

## Statistics

{{ table_stats("lakeparametertypes") }}

## Relationships

**Primary Key**: `lakeparameterid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("lakeparametertypes") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from lakeparametertypes
SELECT *
FROM lakeparametertypes
ORDER BY lakeparameterid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from lakeparametertypes

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM lakeparametertypes;
```

**Purpose**: Get the total number of records in lakeparametertypes

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM lakeparametertypes
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from lakeparametertypes within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by lakeparametercode
SELECT 
    lakeparametercode,
    COUNT(*) as count
FROM lakeparametertypes
GROUP BY lakeparametercode
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by lakeparametercode

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
