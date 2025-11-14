---
title: Samples
description: This table stores sample data. Samples belong to Analysis Units, which belong to Collection Units, w
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.samples`

## Description

This table stores sample data. Samples belong to Analysis Units, which belong to Collection Units, which belong to Sites. Samples also belong to a Dataset, and the Dataset determines the type of sample. Thus, there could be two different samples from the same Analysis Unit, one belonging to a pollen dataset, the other to a plant macrofossil dataset.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esamples-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/samples.html)

{{ table_structure("samples") }}

## Statistics

{{ table_stats("samples") }}

## Relationships

**Primary Key**: `sampleid`

**Foreign Keys**:

- `analysisunitid` → [`analysisunits.analysisunitid`](analysisunits.md)
- `datasetid` → [`datasets.datasetid`](datasets.md)
- `taxonid` → [`taxa.taxonid`](taxa.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("samples") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from samples
SELECT *
FROM samples
ORDER BY sampleid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from samples

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM samples;
```

**Purpose**: Get the total number of records in samples

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM samples
WHERE analysisdate >= '2024-01-01'
  AND analysisdate < '2025-01-01'
ORDER BY analysisdate DESC;
```

**Purpose**: Retrieve records from samples within a specific date range

### Example 4: Join with analysisunits

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM samples t1
INNER JOIN analysisunits t2 
    ON t1.analysisunitid = t2.analysisunitid
LIMIT 100;
```

**Purpose**: Retrieve samples records with related data from analysisunits

### Example 5: Aggregate Data

```sql
-- Aggregate records by analysisunitid
SELECT 
    analysisunitid,
    COUNT(*) as count
FROM samples
GROUP BY analysisunitid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by analysisunitid

**TODO**: Add more specific examples relevant to common research questions or operational tasks.

## Data Quality Notes
### Automated Data Quality Tests

This table is subject to the following automated quality checks:

**❌ ref_001**: datasets_referenced_by_samples

- **Severity**: ERROR
- **Status**: FAILED
- **Description**: All datasets should be referenced by at least one sample

**✅ ref_002**: samples_have_valid_datasets

- **Severity**: ERROR
- **Status**: PASSED
- **Description**: All samples must reference valid collection sites

**❌ comp_002**: samples_have_dates

- **Severity**: WARNING
- **Status**: UNKNOWN
- **Description**: Samples should have collection dates

**❌ biz_001**: modern_samples_have_recent_dates

- **Severity**: WARNING
- **Status**: UNKNOWN
- **Description**: Samples marked as modern should have dates after 1950


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
