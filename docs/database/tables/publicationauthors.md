---
title: Publicationauthors
description: This table lists authors as their names are given in publications. Only the initials are stored for 
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.publicationauthors`

## Description

This table lists authors as their names are given in publications. Only the initials are stored for authors’ given names. The ContactID links to the author’s full name and contact data in the Contacts table. Thus, for a bibliographic entry, Charles Robert Darwin is listed as C. R. Darwin, or as C. Darwin if the publication did not include his middle name. Book editors are also stored in this table if the entire book is cited. However, if a book chapter or section is cited, authors are stored in this table, but the book editors are stored in the PublicationEditors table. Thus, for the following reference, G. C. Frison is stored in the PublicationAuthors table.
Frison, G. C., editor. 1996. The Mill Iron site. University of New Mexico Press, Albuquerque, New Mexico, USA.
Whereas for the following publication, L. S. Cummings is listed in the PublicationAuthors table, and G. C. Frison is listed in the PublicationEditors table.
Cummings, L. S. 1996. Paleoenvironmental interpretations for the Mill Iron site: stratigraphic pollen and phyrolith analysis. Pages 177-193 in G. C. Frison, editor. The Mill Iron site. University of New Mexico Press, Albuquerque, New Mexico, USA.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2epublicationauthors-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/publicationauthors.html)

{{ table_structure("publicationauthors") }}

## Statistics

{{ table_stats("publicationauthors") }}

## Relationships

**Primary Key**: `authorid`

**Foreign Keys**:

- `contactid` → [`contacts.contactid`](contacts.md)
- `publicationid` → [`publications.publicationid`](publications.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("publicationauthors") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from publicationauthors
SELECT *
FROM publicationauthors
ORDER BY authorid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from publicationauthors

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM publicationauthors;
```

**Purpose**: Get the total number of records in publicationauthors

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM publicationauthors
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from publicationauthors within a specific date range

### Example 4: Join with contacts

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM publicationauthors t1
INNER JOIN contacts t2 
    ON t1.contactid = t2.contactid
LIMIT 100;
```

**Purpose**: Retrieve publicationauthors records with related data from contacts

### Example 5: Aggregate Data

```sql
-- Aggregate records by publicationid
SELECT 
    publicationid,
    COUNT(*) as count
FROM publicationauthors
GROUP BY publicationid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by publicationid

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
