---
title: Datasetsubmissions
description: Submissions to the database are of Datasets. Submissions may be original submissions, resubmissions,
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.datasetsubmissions`

## Description

Submissions to the database are of Datasets. Submissions may be original submissions, resubmissions, compilations from other databases, or recompilations. See the description of the DatasetSubmissionTypes table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2edatasetsubmissions-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/datasetsubmissions.html)

{{ table_structure("datasetsubmissions") }}

## Statistics

{{ table_stats("datasetsubmissions") }}

## Relationships

**Primary Key**: `submissionid`

**Foreign Keys**:

- `databaseid` → [`constituentdatabases.databaseid`](constituentdatabases.md)
- `contactid` → [`contacts.contactid`](contacts.md)
- `datasetid` → [`datasets.datasetid`](datasets.md)
- `submissiontypeid` → [`datasetsubmissiontypes.submissiontypeid`](datasetsubmissiontypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("datasetsubmissions") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from datasetsubmissions
SELECT *
FROM datasetsubmissions
ORDER BY submissionid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from datasetsubmissions

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM datasetsubmissions;
```

**Purpose**: Get the total number of records in datasetsubmissions

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM datasetsubmissions
WHERE submissiondate >= '2024-01-01'
  AND submissiondate < '2025-01-01'
ORDER BY submissiondate DESC;
```

**Purpose**: Retrieve records from datasetsubmissions within a specific date range

### Example 4: Join with constituentdatabases

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM datasetsubmissions t1
INNER JOIN constituentdatabases t2 
    ON t1.databaseid = t2.databaseid
LIMIT 100;
```

**Purpose**: Retrieve datasetsubmissions records with related data from constituentdatabases

### Example 5: Aggregate Data

```sql
-- Aggregate records by datasetid
SELECT 
    datasetid,
    COUNT(*) as count
FROM datasetsubmissions
GROUP BY datasetid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by datasetid

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
