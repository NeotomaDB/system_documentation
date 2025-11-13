---
title: Ecolgroups
description: Taxa are assigned to Sets of Ecological Groups. A taxon may be assigned to more than one Set of Ecol
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.ecolgroups`

## Description

Taxa are assigned to Sets of Ecological Groups. A taxon may be assigned to more than one Set of Ecological Groups, representing different schemes for organizing taxa.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eecolgroups-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/ecolgroups.html)

{{ table_structure("ecolgroups") }}

## Statistics

{{ table_stats("ecolgroups") }}

## Relationships

**Primary Key**: `taxonid, ecolsetid`

**Foreign Keys**:

- `ecolgroupid` → [`ecolgrouptypes.ecolgroupid`](ecolgrouptypes.md)
- `ecolsetid` → [`ecolsettypes.ecolsetid`](ecolsettypes.md)
- `taxonid` → [`taxa.taxonid`](taxa.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("ecolgroups") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from ecolgroups
SELECT *
FROM ecolgroups
ORDER BY taxonid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from ecolgroups

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM ecolgroups;
```

**Purpose**: Get the total number of records in ecolgroups

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM ecolgroups
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from ecolgroups within a specific date range

### Example 4: Join with ecolgrouptypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM ecolgroups t1
INNER JOIN ecolgrouptypes t2 
    ON t1.ecolgroupid = t2.ecolgroupid
LIMIT 100;
```

**Purpose**: Retrieve ecolgroups records with related data from ecolgrouptypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by ecolsetid
SELECT 
    ecolsetid,
    COUNT(*) as count
FROM ecolgroups
GROUP BY ecolsetid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by ecolsetid

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
