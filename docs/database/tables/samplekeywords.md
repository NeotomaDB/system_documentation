---
title: Samplekeywords
description: This table lists the Sample Analysts.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.samplekeywords`

## Description

This table lists the Sample Analysts.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2esamplekeywords-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/samplekeywords.html)

{{ table_structure("samplekeywords") }}

## Statistics

{{ table_stats("samplekeywords") }}

## Relationships

**Primary Key**: `sampleid, keywordid`

**Foreign Keys**:

- `keywordid` → [`keywords.keywordid`](keywords.md)
- `sampleid` → [`samples.sampleid`](samples.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("samplekeywords") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from samplekeywords
SELECT *
FROM samplekeywords
ORDER BY sampleid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from samplekeywords

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM samplekeywords;
```

**Purpose**: Get the total number of records in samplekeywords

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM samplekeywords
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from samplekeywords within a specific date range

### Example 4: Join with keywords

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM samplekeywords t1
INNER JOIN keywords t2 
    ON t1.keywordid = t2.keywordid
LIMIT 100;
```

**Purpose**: Retrieve samplekeywords records with related data from keywords

### Example 5: Aggregate Data

```sql
-- Aggregate records by keywordid
SELECT 
    keywordid,
    COUNT(*) as count
FROM samplekeywords
GROUP BY keywordid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by keywordid

**TODO**: Add more specific examples relevant to common research questions or operational tasks.

## Data Quality Notes
### Automated Data Quality Tests

This table is subject to the following automated quality checks:

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
