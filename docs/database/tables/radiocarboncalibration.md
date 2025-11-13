---
title: Radiocarboncalibration
description: Radiocarbon calibration table. This table is intended for quick calibration of age-model radiocarbon
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.radiocarboncalibration`

## Description

Radiocarbon calibration table. This table is intended for quick calibration of age-model radiocarbon dates. These calibrated dates are for perusal and data exploration only. Please see Section 2.5 for a full discussion.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eradiocarboncalibration-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/radiocarboncalibration.html)

{{ table_structure("radiocarboncalibration") }}

## Statistics

{{ table_stats("radiocarboncalibration") }}

## Relationships

**Primary Key**: `c14yrbp`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("radiocarboncalibration") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from radiocarboncalibration
SELECT *
FROM radiocarboncalibration
ORDER BY c14yrbp DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from radiocarboncalibration

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM radiocarboncalibration;
```

**Purpose**: Get the total number of records in radiocarboncalibration

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
