---
title: Collectionunits
description: This table stores data for Collection Units.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.collectionunits`

## Description

This table stores data for Collection Units.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2ecollectionunits-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/collectionunits.html)

{{ table_structure("collectionunits") }}

## Statistics

{{ table_stats("collectionunits") }}

## Relationships

**Primary Key**: `collectionunitid`

**Foreign Keys**:

- `colltypeid` → [`collectiontypes.colltypeid`](collectiontypes.md)
- `depenvtid` → [`depenvttypes.depenvtid`](depenvttypes.md)
- `substrateid` → [`rocktypes.rocktypeid`](rocktypes.md)
- `siteid` → [`sites.siteid`](sites.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("collectionunits") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from collectionunits
SELECT *
FROM collectionunits
ORDER BY collectionunitid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from collectionunits

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM collectionunits;
```

**Purpose**: Get the total number of records in collectionunits

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM collectionunits
WHERE colldate >= '2024-01-01'
  AND colldate < '2025-01-01'
ORDER BY colldate DESC;
```

**Purpose**: Retrieve records from collectionunits within a specific date range

### Example 4: Join with collectiontypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM collectionunits t1
INNER JOIN collectiontypes t2 
    ON t1.colltypeid = t2.colltypeid
LIMIT 100;
```

**Purpose**: Retrieve collectionunits records with related data from collectiontypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by handle
SELECT 
    handle,
    COUNT(*) as count
FROM collectionunits
GROUP BY handle
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by handle

**TODO**: Add more specific examples relevant to common research questions or operational tasks.

## Data Quality Notes
### Automated Data Quality Tests

This table is subject to the following automated quality checks:

**❌ ref_003**: sites_have_collection_units

- **Severity**: ERROR
- **Status**: FAILED
- **Description**: All sites should have at least one collection unit.

- **Suggested Remediation**: - Remove "floating" sites.
- Ensure that the collection units have not been accidentally deleted.


**❌ comp_002**: collectionunits_have_dates

- **Severity**: WARNING
- **Status**: FAILED
- **Description**: collectionunits should have collection dates

- **Suggested Remediation**: - Review original data sources for date information.
- Derive dates from publications where available.
- Record the decision making processes at a Constituent Database level. 


**✅ comp_004**: sample_ages_for_samples

- **Severity**: WARNING
- **Status**: PASSED
- **Description**: Samples should have sample ages, whether from a chronology or collection date.


See the [Data Quality Report](../../reports/data_quality_report.md) for details.
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
