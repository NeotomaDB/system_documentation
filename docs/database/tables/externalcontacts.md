---
title: Externalcontacts
description: No description available in database.
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.externalcontacts`

## Description

No description available in database.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2eexternalcontacts-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/externalcontacts.html)

{{ table_structure("externalcontacts") }}

## Statistics

{{ table_stats("externalcontacts") }}

## Relationships

**Foreign Keys**:

- `contactid` → [`contacts.contactid`](contacts.md)
- `extdatabaseid` → [`externaldatabases.extdatabaseid`](externaldatabases.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("externalcontacts") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from externalcontacts
SELECT *
FROM externalcontacts
ORDER BY contactid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from externalcontacts

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM externalcontacts;
```

**Purpose**: Get the total number of records in externalcontacts

### Example 3: Join with contacts

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM externalcontacts t1
INNER JOIN contacts t2 
    ON t1.contactid = t2.contactid
LIMIT 100;
```

**Purpose**: Retrieve externalcontacts records with related data from contacts

### Example 4: Aggregate Data

```sql
-- Aggregate records by identifier
SELECT 
    identifier,
    COUNT(*) as count
FROM externalcontacts
GROUP BY identifier
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by identifier

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
