---
title: Specimengenbank
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.specimengenbank`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2especimengenbank-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/specimengenbank.html)

{{ table_structure("specimengenbank") }}

## Statistics

{{ table_stats("specimengenbank") }}

## Relationships

**Primary Key**: `specimenid, genbanknr`

**Foreign Keys**:

- `specimenid` → [`specimens.specimenid`](specimens.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("specimengenbank") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from specimengenbank
SELECT *
FROM specimengenbank
ORDER BY specimenid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from specimengenbank

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM specimengenbank;
```

**Purpose**: Get the total number of records in specimengenbank

### Example 3: Join with specimens

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM specimengenbank t1
INNER JOIN specimens t2 
    ON t1.specimenid = t2.specimenid
LIMIT 100;
```

**Purpose**: Retrieve specimengenbank records with related data from specimens

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
