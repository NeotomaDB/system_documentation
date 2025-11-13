---
title: Data
description: The primary data table in the database. Each occurrence of a Variable in a sample comprises a record
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.data`

## Description

The primary data table in the database. Each occurrence of a Variable in a sample comprises a record in the Data table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2edata-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/data.html)

{{ table_structure("data") }}

## Statistics

{{ table_stats("data") }}

## Relationships

**Primary Key**: `dataid`

**Foreign Keys**:

- `sampleid` → [`samples.sampleid`](samples.md)
- `variableid` → [`variables.variableid`](variables.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("data") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from data
SELECT *
FROM data
ORDER BY dataid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from data

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM data;
```

**Purpose**: Get the total number of records in data

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM data
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from data within a specific date range

### Example 4: Join with samples

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM data t1
INNER JOIN samples t2 
    ON t1.sampleid = t2.sampleid
LIMIT 100;
```

**Purpose**: Retrieve data records with related data from samples

### Example 5: Aggregate Data

```sql
-- Aggregate records by sampleid
SELECT 
    sampleid,
    COUNT(*) as count
FROM data
GROUP BY sampleid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by sampleid

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
