---
title: [Table Name]
description: Brief description of the table
status: draft
last_validated: YYYY-MM-DD
row_count: 0
---

# Table: `table_name`

## Description

[Comprehensive description of what this table stores, its purpose, and how it relates to the research]

## Table Structure

{{ table_structure("table_name") }}

## Statistics

{{ table_stats("table_name") }}

## Relationships

[Describe foreign key relationships and how this table connects to others]

**Related Tables:**
- [`related_table_1`](related_table_1.md) - Description of relationship
- [`related_table_2`](related_table_2.md) - Description of relationship

## Data Dictionary

{{ table_columns("table_name") }}

## Usage Examples

### Example 1: Basic Selection

[Selection description]

```sql
-- Get all records from the last year
SELECT *
FROM table_name
WHERE created_date >= CURRENT_DATE - INTERVAL '1 year'
ORDER BY created_date DESC
LIMIT 100;
```

### Example 2: `JOIN`s and `FILTER`s

```sql
```

Purpose: [Explain what this query does and when to use it]

## Data Quality Notes

[Any known data quality issues]
[Validation rules]
[Update frequency]

## Maintenance

Data Owner: [Team/Person responsible]
Update Frequency: [e.g., Real-time, Daily, Weekly]
Last Major Schema Change: [Date and description]

---
Last validated: {{ last_validated() }} | Documentation status: {{ doc_status("table_name") }}

### `docs/database/tables/.pages`

```yaml
title: Database Tables
nav:
  - Overview: ../overview.md
  - ...  # This will auto-include all other .md files
