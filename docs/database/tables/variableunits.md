---
title: Variableunits
description: Lookup table of Variable Units. Table is referenced by the Variables table.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.variableunits`

## Description

Lookup table of Variable Units. Table is referenced by the Variables table.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2evariableunits-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/variableunits.html)

{{ table_structure("variableunits") }}

## Statistics

{{ table_stats("variableunits") }}

## Relationships

**Primary Key**: `variableunitsid`

No foreign key relationships.

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("variableunits") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from variableunits
SELECT *
FROM variableunits
ORDER BY variableunitsid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from variableunits

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM variableunits;
```

**Purpose**: Get the total number of records in variableunits

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM variableunits
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from variableunits within a specific date range

### Example 4: Aggregate Data

```sql
-- Aggregate records by variableunits
SELECT 
    variableunits,
    COUNT(*) as count
FROM variableunits
GROUP BY variableunits
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by variableunits

**TODO**: Add more specific examples relevant to common research questions or operational tasks.

## Data Quality Notes
### Automated Data Quality Tests

This table is subject to the following automated quality checks:

**❌ bix_003**: variable_elements_in_use

- **Severity**: WARNING
- **Status**: FAILED
- **Description**: Over time a number of variable contexts, units and elements have been created but not neccessarily used. In some cases this may have resulted from improperly entered data 
in the Tilia spreadsheet.


- **Suggested Remediation**: - Where possible, remove unused units/elements/contexts - Ensure any near-duplicates of existing units/elements/contexts are using best-practice or accepted notations.



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
