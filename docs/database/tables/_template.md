
```markdown
---
title: [Table Name]
description: Brief description of the table
status: draft  # draft, review, complete
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

```sql
-- Get all records from the last year
SELECT *
FROM table_name
WHERE created_date >= CURRENT_DATE - INTERVAL '1 year'
ORDER BY created_date DESC
LIMIT 100;
```

**Purpose**: [Explain what this query does and when to use it]

### Example 2: Join with Related Tables

```sql
-- Join example
SELECT 
    t1.column_a,
    t2.column_b,
    COUNT(*) as count
FROM table_name t1
INNER JOIN related_table t2 ON t1.id = t2.table_name_id
GROUP BY t1.column_a, t2.column_b
ORDER BY count DESC;
```

**Purpose**: [Explain what this query does and when to use it]

### Example 3: Common Aggregation

```sql
-- Aggregation example
SELECT 
    DATE_TRUNC('month', observation_date) as month,
    COUNT(*) as observations,
    COUNT(DISTINCT observer_id) as unique_observers
FROM table_name
WHERE observation_date >= '2023-01-01'
GROUP BY DATE_TRUNC('month', observation_date)
ORDER BY month;
```

**Purpose**: [Explain what this query does and when to use it]

## Data Quality Notes

- [Any known data quality issues]
- [Validation rules]
- [Update frequency]

## Maintenance

- **Data Owner**: [Team/Person responsible]
- **Update Frequency**: [e.g., Real-time, Daily, Weekly]
- **Last Major Schema Change**: [Date and description]

---

*Last validated: {{ last_validated() }} | Documentation status: {{ doc_status("table_name") }}*
