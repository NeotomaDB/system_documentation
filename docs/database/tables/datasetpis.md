---
title: Datasetpis
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.datasetpis`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2edatasetpis-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/datasetpis.html)

{{ table_structure("datasetpis") }}

## Statistics

{{ table_stats("datasetpis") }}

## Relationships

**Foreign Keys**:

- `contactid` → [`contacts.contactid`](contacts.md)
- `datasetid` → [`datasets.datasetid`](datasets.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("datasetpis") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from datasetpis
SELECT *
FROM datasetpis
ORDER BY datasetid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from datasetpis

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM datasetpis;
```

**Purpose**: Get the total number of records in datasetpis

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM datasetpis
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from datasetpis within a specific date range

### Example 4: Join with contacts

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM datasetpis t1
INNER JOIN contacts t2 
    ON t1.contactid = t2.contactid
LIMIT 100;
```

**Purpose**: Retrieve datasetpis records with related data from contacts

### Example 5: Aggregate Data

```sql
-- Aggregate records by contactid
SELECT 
    contactid,
    COUNT(*) as count
FROM datasetpis
GROUP BY contactid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by contactid

**TODO**: Add more specific examples relevant to common research questions or operational tasks.

## Data Quality Notes
### Automated Data Quality Tests

This table is subject to the following automated quality checks:

**❌ comp_001**: datasets_have_investigators

- **Severity**: WARNING
- **Status**: UNKNOWN
- **Description**: Datasets should have at least one principal investigator


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
