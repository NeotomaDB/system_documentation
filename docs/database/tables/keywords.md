---
title: Keywords
description: Lookup table of Keywords referenced by the SampleKeywords table. The table provides a means to ident
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.keywords`

## Description

Lookup table of Keywords referenced by the SampleKeywords table. The table provides a means to identify samples sharing a common attribute. For example, the keyword «modern sample» identifies modern surface samples in the database. These samples include individual surface samples, as well as core tops. Although not implemented, a «pre-European settlement» keyword would be a means to identify samples just predating European settlement.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2ekeywords-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/keywords.html)

{{ table_structure("keywords") }}

## Statistics

{{ table_stats("keywords") }}

## Relationships

**Primary Key**: `keywordid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("keywords") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from keywords
SELECT *
FROM keywords
ORDER BY keywordid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from keywords

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM keywords;
```

**Purpose**: Get the total number of records in keywords

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM keywords
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from keywords within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by keyword
SELECT 
    keyword,
    COUNT(*) as count
FROM keywords
GROUP BY keyword
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by keyword

**TODO**: Add more specific examples relevant to common research questions or operational tasks.

## Data Quality Notes
### Automated Data Quality Tests

This table is subject to the following automated quality checks:

**✅ biz_001**: modern_samples_have_recent_dates

- **Severity**: WARNING
- **Status**: PASSED
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
