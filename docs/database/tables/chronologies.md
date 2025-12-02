---
title: Chronologies
description: This table stores Chronology data. A Chronology refers to an explicit chronology assigned to a Colle
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.chronologies`

## Description

This table stores Chronology data. A Chronology refers to an explicit chronology assigned to a Collection Unit. A Chronology has Chronology Controls, the actual age-depth control points, which are stored in the ChronControls table. A Chronology is also based on an Age Model, which may be a numerical method that fits a curve to a set of age-depth control points or may simply be individually dated Analysis Units.
A Collection Unit may have more than one Chronology, for example one in radiocarbon years and another in calibrated radiocarbon years. There may be a Chronology developed by the original author and another developed by a later research project. Chronologies may be stored for archival reasons, even though they are now believed to have problems, if they were used for an important research project. One Chronology per Age Type may be designated the default Chronology, which is the Chronology currently preferred by the database stewards.
Based upon the Chronology, which includes the Age Model and the Chron Controls, ages are assigned to individual samples, which are stored in the SampleAges table.
A younger and older age bounds are assigned to the Chronology. Within these bounds the Chronology is regarded as reliable. Ages may be assigned to samples beyond the reliable age bounds, but these are not considered reliable

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2echronologies-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/chronologies.html)

{{ table_structure("chronologies") }}

## Statistics

{{ table_stats("chronologies") }}

## Relationships

**Primary Key**: `chronologyid`

**Foreign Keys**:

- `agetypeid` → [`agetypes.agetypeid`](agetypes.md)
- `collectionunitid` → [`collectionunits.collectionunitid`](collectionunits.md)
- `contactid` → [`contacts.contactid`](contacts.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("chronologies") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from chronologies
SELECT *
FROM chronologies
ORDER BY chronologyid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from chronologies

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM chronologies;
```

**Purpose**: Get the total number of records in chronologies

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM chronologies
WHERE dateprepared >= '2024-01-01'
  AND dateprepared < '2025-01-01'
ORDER BY dateprepared DESC;
```

**Purpose**: Retrieve records from chronologies within a specific date range

### Example 4: Join with agetypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM chronologies t1
INNER JOIN agetypes t2 
    ON t1.agetypeid = t2.agetypeid
LIMIT 100;
```

**Purpose**: Retrieve chronologies records with related data from agetypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by collectionunitid
SELECT 
    collectionunitid,
    COUNT(*) as count
FROM chronologies
GROUP BY collectionunitid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by collectionunitid

**TODO**: Add more specific examples relevant to common research questions or operational tasks.

## Data Quality Notes
### Automated Data Quality Tests

This table is subject to the following automated quality checks:

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
