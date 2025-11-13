---
title: Publications
description: This table stores publication or bibliographic data. The table is designed with fields for bibliogra
status: draft
last_validated: 2025-11-12
---

# Table: `ndb.publications`

## Description

This table stores publication or bibliographic data. The table is designed with fields for bibliographic data so that bibliographies can be formatted in different styles and potentially exported to bibliographic software such EndNote®. In the constituent databases that were originally merged into Neotoma, bibliographic entries were not parsed into separate fields, but rather were stored as free-form text. Because complete parsing of these thousands of legacy bibliographic entries into individual fields would have been prohibitively time consuming, the existing bibliographic data were ingested “as is” with a PubTypeID = Other. However, for legacy publications, the year of publication was added to the Year field, and authors were parsed into the PublicationAuthors table and added to the Contacts table. In addition, some global changes were made. For example, «Pp.» was changed to «Pages», «Ed.» to «Editor», and «Eds.» to «Editors». Also for FAUNMAP entries, abbreviated journal names were changed to fully spelled out names.
The merged databases used different bibliographic styles, and data entry personnel working on the same database sometimes followed different conventions. Consequently, the current bibliographic entries are not stylistically uniform. Eventually, the legacy bibliographic data will be parsed into separate fields.
The Publications table has fields to accommodate a number of different types of publications. Some fields contain different kinds of data for different kinds of publications. For example, the BookTitle field stores the titles of books, but stores the journal name for journal articles. The Publisher field stores the name of the publisher for books, but the name of the university for theses and dissertations.
Authors are stored in the PublicationAuthors table. Editors are also stored in the PublicationAuthors table if the entire publication is cited. The PublicationAuthors table has a ContactID field, which links to the Contacts table, where full names and contact information is stored for authors and editors. The PubTypeID «Authored Book» or «Edited Book» indicates whether the Publication Authors records are authors or editors. If a book chapter or section is the primary bibliographic entry, then the book editors are stored in the PublicationEditors table, which does not have a ContactID field.

**TODO**: Expand this description with:
- What data does this table store?
- What is the business/research purpose?
- How is this data collected or generated?
- Are there any important caveats or data quality issues?

## Table Structure

[![Visual Schema](https://img.shields.io/badge/Visual_Schema-ndb%2epublications-blue?style=flat-square)](https://open.neotomadb.org/dbschema/ndb/publications.html)

{{ table_structure("publications") }}

## Statistics

{{ table_stats("publications") }}

## Relationships

**Primary Key**: `publicationid`

**Foreign Keys**:

- `pubtypeid` → [`publicationtypes.pubtypeid`](publicationtypes.md)

**Referenced By**:

**TODO**: Document which tables reference this table (will be auto-detected in validation).

## Data Dictionary

{{ table_columns("publications") }}

**TODO**: Review column descriptions and add comments where missing.

## Usage Examples

### Example 1: Basic Selection

```sql
-- Get recent records from publications
SELECT *
FROM publications
ORDER BY publicationid DESC
LIMIT 10;
```

**Purpose**: Retrieve the 10 most recent records from publications

### Example 2: Count Records

```sql
-- Count total records
SELECT COUNT(*) as total_records
FROM publications;
```

**Purpose**: Get the total number of records in publications

### Example 3: Filter by Date Range

```sql
-- Get records within a date range
SELECT *
FROM publications
WHERE recdatecreated >= '2024-01-01'
  AND recdatecreated < '2025-01-01'
ORDER BY recdatecreated DESC;
```

**Purpose**: Retrieve records from publications within a specific date range

### Example 4: Join with publicationtypes

```sql
-- Join with related table
SELECT 
    t1.*,
    t2.*
FROM publications t1
INNER JOIN publicationtypes t2 
    ON t1.pubtypeid = t2.pubtypeid
LIMIT 100;
```

**Purpose**: Retrieve publications records with related data from publicationtypes

### Example 5: Aggregate Data

```sql
-- Aggregate records by pubtypeid
SELECT 
    pubtypeid,
    COUNT(*) as count
FROM publications
GROUP BY pubtypeid
ORDER BY count DESC
LIMIT 10;
```

**Purpose**: Count records grouped by pubtypeid

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
