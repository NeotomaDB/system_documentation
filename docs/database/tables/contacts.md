---
title: Contacts
description: This table lists persons and organizations referenced by the Chronologies, Collectors, DatasetPIs, D
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.contacts`

## Description

This table lists persons and organizations referenced by the Chronologies, Collectors, DatasetPIs, DatasetSubmissions, Projects, PublicationAuthors, SampleAnalysts, and SiteImages tables.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2econtacts-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/contacts.html)

{{ table_structure("contacts") }}

## Statistics

{{ table_stats("contacts") }}

## Relationships

**Primary Key**: `contactid`

**Foreign Keys**:

- `contactstatusid` → [`contactstatuses.contactstatusid`](contactstatuses.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("contacts") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from contacts
SELECT *
FROM contacts
ORDER BY contactid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from contacts

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM contacts;
```

**Purpose**: Get the total number of records in contacts

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM contacts
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from contacts within a specific date range

### Example 4: Join with contactstatuses

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM contacts t1
INNER JOIN contactstatuses t2 
    ON t1.contactstatusid = t2.contactstatusid
LIMIT 100;
```

**Purpose**: Retrieve contacts records with related data from contactstatuses

### Example 5: Aggregate Data

```sql
-- Aggregate records by aliasid
SELECT 
    aliasid,
    COUNT(*) as count
FROM contacts
GROUP BY aliasid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by aliasid

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
