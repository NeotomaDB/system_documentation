---
title: Datauncertainties
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.datauncertainties`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2edatauncertainties-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/datauncertainties.html)

{{ table_structure("datauncertainties") }}

## Statistics

{{ table_stats("datauncertainties") }}

## Relationships

**Foreign Keys**:

- `dataid` → [`data.dataid`](data.md)
- `uncertaintyunitid` → [`variableunits.variableunitsid`](variableunits.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("datauncertainties") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from datauncertainties
SELECT *
FROM datauncertainties
ORDER BY dataid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from datauncertainties

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM datauncertainties;
```

**Purpose**: Get the total number of records in datauncertainties

### Example 3: Join with data

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM datauncertainties t1
INNER JOIN data t2 
    ON t1.dataid = t2.dataid
LIMIT 100;
```

**Purpose**: Retrieve datauncertainties records with related data from data

### Example 4: Aggregate Data

```sql
-- Aggregate records by uncertaintyvalue
SELECT 
    uncertaintyvalue,
    COUNT(*) as count
FROM datauncertainties
GROUP BY uncertaintyvalue
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by uncertaintyvalue

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
