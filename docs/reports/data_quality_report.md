# Data Quality Report

**Generated**: 2025-12-01 16:46:52

## Summary

- **Total Tests**: 16
- **Passed**: 6 ✓
- **Failed**: 10 ✗
- **Pass Rate**: 37.5%

## Referential Integrity

**Pass Rate**: 2/4

### ❌ Failed Tests

#### ref_001: datasets_referenced_by_samples

**Severity**: ERROR

**Description**: All datasets should be referenced by at least one sample

**Affected Tables**: `datasets`, `samples`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: datasets_referenced_by_samples (ref_001)
  Category: referential_integrity
  ================================================================================
  Description: All datasets should be referenced by at least one sample
  
  Rationale: Every dataset should have associated samples. A dataset without samples
  indicates either incomplete data entry or orphaned records.
  
  
  Expected: No violations
  Found: 99 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'datasetid': 16232, 'datasetname': 'Rio Dell Assemblage'})
  RealDictRow({'datasetid': 18052, 'datasetname': 'Halifax Lakes'})
  RealDictRow({'datasetid': 18053, 'datasetname': 'Halifax Lakes'})
  RealDictRow({'datasetid': 21425, 'datasetname': 'gravity corer'})
  RealDictRow({'datasetid': 21673, 'datasetname': 'Rusk County ANSP'})
  RealDictRow({'datasetid': 22700, 'datasetname': None})
  RealDictRow({'datasetid': 22702, 'datasetname': None})
  RealDictRow({'datasetid': 24307, 'datasetname': 'EPD E# 1080'})
  RealDictRow({'datasetid': 24309, 'datasetname': 'EPD E# 1082'})
  RealDictRow({'datasetid': 24310, 'datasetname': 'EPD E# 1082'})
assert 99 == 0
 +  where 99 = len([RealDictRow({'datasetid': 16232, 'datasetname': 'Rio Dell Assemblage'}), RealDictRow({'datasetid': 18052, 'datasetname': 'Halifax Lakes'}), RealDictRow({'datasetid': 18053, 'datasetname': 'Halifax Lakes'}), RealDictRow({'datasetid': 21425, 'datasetname': 'gravity corer'}), RealDictRow({'datasetid': 21673, 'datasetname': 'Rusk County ANSP'}), RealDictRow({'datasetid': 22700, 'datasetname': None}), ...])

**Rationale**: Every dataset should have associated samples. A dataset without samples
indicates either incomplete data entry or orphaned records.


**Remediation**:
- Check if samples were never entered for this dataset
- Verify if dataset should be archived/deleted
- Contact data owner for clarification


---

#### ref_003: sites_have_collection_units

**Severity**: ERROR

**Description**: All sites should have at least one collection unit.

**Affected Tables**: `sites`, `collectionunits`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: sites_have_collection_units (ref_003)
  Category: referential_integrity
  ================================================================================
  Description: All sites should have at least one collection unit.
  
  Rationale: All sites should have one collection unit from which samples are obtained.
  
  
  Expected: No violations
  Found: 81 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'siteid': 30939, 'collectionunitid': None})
  RealDictRow({'siteid': 30940, 'collectionunitid': None})
  RealDictRow({'siteid': 30942, 'collectionunitid': None})
  RealDictRow({'siteid': 30953, 'collectionunitid': None})
  RealDictRow({'siteid': 30999, 'collectionunitid': None})
  RealDictRow({'siteid': 31292, 'collectionunitid': None})
  RealDictRow({'siteid': 31408, 'collectionunitid': None})
  RealDictRow({'siteid': 31409, 'collectionunitid': None})
  RealDictRow({'siteid': 31410, 'collectionunitid': None})
  RealDictRow({'siteid': 31411, 'collectionunitid': None})
assert 81 == 0
 +  where 81 = len([RealDictRow({'siteid': 30939, 'collectionunitid': None}), RealDictRow({'siteid': 30940, 'collectionunitid': None}), RealDictRow({'siteid': 30942, 'collectionunitid': None}), RealDictRow({'siteid': 30953, 'collectionunitid': None}), RealDictRow({'siteid': 30999, 'collectionunitid': None}), RealDictRow({'siteid': 31292, 'collectionunitid': None}), ...])

**Rationale**: All sites should have one collection unit from which samples are obtained.


**Remediation**:
- Remove "floating" sites.
- Ensure that the collection units have not been accidentally deleted.


---

### ✅ Passed Tests

- **ref_002**: samples_have_valid_datasets
- **ref_004**: valid_taxa_need_highertaxonids

## Data Completeness

**Pass Rate**: 1/4

### ❌ Failed Tests

#### comp_001: datasets_have_investigators

**Severity**: WARNING

**Description**: Datasets should have at least one principal investigator

**Affected Tables**: `datasets`, `datasetpis`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: datasets_have_investigators (comp_001)
  Category: data_completeness
  ================================================================================
  Description: Datasets should have at least one principal investigator
  
  Rationale: Every dataset should have an associated principal investigator for
  data attribution and contact purposes.
  
  
  Expected: No violations
  Found: 6434 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'datasetid': 6122, 'datasetname': None})
  RealDictRow({'datasetid': 8533, 'datasetname': None})
  RealDictRow({'datasetid': 66609, 'datasetname': None})
  RealDictRow({'datasetid': 10627, 'datasetname': None})
  RealDictRow({'datasetid': 5161, 'datasetname': None})
  RealDictRow({'datasetid': 10876, 'datasetname': None})
  RealDictRow({'datasetid': 6680, 'datasetname': None})
  RealDictRow({'datasetid': 8716, 'datasetname': None})
  RealDictRow({'datasetid': 10293, 'datasetname': None})
  RealDictRow({'datasetid': 9408, 'datasetname': None})
assert 6434 == 0
 +  where 6434 = len([RealDictRow({'datasetid': 6122, 'datasetname': None}), RealDictRow({'datasetid': 8533, 'datasetname': None}), RealDictRow({'datasetid': 66609, 'datasetname': None}), RealDictRow({'datasetid': 10627, 'datasetname': None}), RealDictRow({'datasetid': 5161, 'datasetname': None}), RealDictRow({'datasetid': 10876, 'datasetname': None}), ...])

**Rationale**: Every dataset should have an associated principal investigator for
data attribution and contact purposes.


**Remediation**:
- Research and add PI information
- Contact data owner to identify responsible investigator


---

#### comp_002: collectionunits_have_dates

**Severity**: WARNING

**Description**: collectionunits should have collection dates

**Affected Tables**: `collectionunits`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: collectionunits_have_dates (comp_002)
  Category: data_completeness
  ================================================================================
  Description: collectionunits should have collection dates
  
  Rationale: Collection dates are critical for temporal analysis and data quality.
  
  
  Expected: No violations
  Found: 13637 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'collectionunitid': 1, 'handle': '15-1'})
  RealDictRow({'collectionunitid': 2, 'handle': '15-2'})
  RealDictRow({'collectionunitid': 3, 'handle': '16-1'})
  RealDictRow({'collectionunitid': 4, 'handle': '17-1'})
  RealDictRow({'collectionunitid': 5, 'handle': '17-2'})
  RealDictRow({'collectionunitid': 6, 'handle': '17-3'})
  RealDictRow({'collectionunitid': 7, 'handle': '3PINES'})
  RealDictRow({'collectionunitid': 8, 'handle': 'ABALONE'})
  RealDictRow({'collectionunitid': 10, 'handle': 'ADC001'})
  RealDictRow({'collectionunitid': 11, 'handle': 'ADYCHA'})
assert 13637 == 0
 +  where 13637 = len([RealDictRow({'collectionunitid': 1, 'handle': '15-1'}), RealDictRow({'collectionunitid': 2, 'handle': '15-2'}), RealDictRow({'collectionunitid': 3, 'handle': '16-1'}), RealDictRow({'collectionunitid': 4, 'handle': '17-1'}), RealDictRow({'collectionunitid': 5, 'handle': '17-2'}), RealDictRow({'collectionunitid': 6, 'handle': '17-3'}), ...])

**Rationale**: Collection dates are critical for temporal analysis and data quality.


**Remediation**:
- Review original data sources for date information.
- Derive dates from publications where available.
- Record the decision making processes at a Constituent Database level. 


---

#### comp_003: taxa_have_been_added_by_stewards

**Severity**: WARNING

**Description**: When a taxon is submitted to Neotoma there should be a person associated with that submission

**Affected Tables**: `taxa`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: taxa_have_been_added_by_stewards (comp_003)
  Category: data_completeness
  ================================================================================
  Description: When a taxon is submitted to Neotoma there should be a person associated with that submission
  
  Rationale: We should know who placed a taxon into the hierarchy so we have some background on any decision making or choices that defined that placement.
  
  
  Expected: No violations
  Found: 5189 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'taxonid': 30})
  RealDictRow({'taxonid': 63})
  RealDictRow({'taxonid': 6261})
  RealDictRow({'taxonid': 96})
  RealDictRow({'taxonid': 97})
  RealDictRow({'taxonid': 184})
  RealDictRow({'taxonid': 2140})
  RealDictRow({'taxonid': 276})
  RealDictRow({'taxonid': 296})
  RealDictRow({'taxonid': 305})
assert 5189 == 0
 +  where 5189 = len([RealDictRow({'taxonid': 30}), RealDictRow({'taxonid': 63}), RealDictRow({'taxonid': 6261}), RealDictRow({'taxonid': 96}), RealDictRow({'taxonid': 97}), RealDictRow({'taxonid': 184}), ...])

**Rationale**: We should know who placed a taxon into the hierarchy so we have some background on any decision making or choices that defined that placement.


**Remediation**:
- Confirm placement with stewards, identify those stewards as the
validators.


---

### ✅ Passed Tests

- **comp_004**: sample_ages_for_samples

## Data Validity

**Pass Rate**: 2/5

### ❌ Failed Tests

#### valid_003: valid_terminal_taxa_have_values

**Severity**: WARNING

**Description**: Taxa that are identified as 'leaves' in the database should be associated with values in the database.

**Affected Tables**: `taxa`, `variables`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: valid_terminal_taxa_have_values (valid_003)
  Category: data_validity
  ================================================================================
  Description: Taxa that are identified as 'leaves' in the database should be associated with values in the database.
  
  Rationale: If a taxon was entered into the database as a terminal leaf in the hierarchy, it ought to be associated with some data entry. If it is
  absent from the variables table, then it was entered and never used.
  
  
  Expected: No violations
  Found: 17761 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'taxonid': 183, 'taxoncode': '[Mimdae]', 'taxonname': 'Mimosoideae', 'author': 'de Candolle, 1825', 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 9757, 'validatorid': 44, 'validatedate': datetime.date(2020, 7, 27), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2020, 7, 27, 2, 4, 41), 'count': 0})
  RealDictRow({'taxonid': 187, 'taxoncode': 'Bryida.ud', 'taxonname': 'Bryopsida undiff.', 'author': 'Pax, 1900', 'valid': True, 'highertaxonid': 659, 'extinct': False, 'taxagroupid': 'BRY', 'publicationid': 311, 'validatorid': 44, 'validatedate': datetime.date(2015, 1, 3), 'notes': None, 'recdatecreated': datetime.datetime(2013, 1, 1, 0, 0), 'recdatemodified': datetime.datetime(2015, 1, 3, 16, 55, 26), 'count': 0})
  RealDictRow({'taxonid': 196, 'taxoncode': '[Osu.ud]', 'taxonname': 'Osmunda undiff.', 'author': 'Linnaeus, 1753', 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 9777, 'validatorid': 44, 'validatedate': datetime.date(2017, 4, 5), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2017, 4, 5, 18, 44, 51), 'count': 0})
  RealDictRow({'taxonid': 227, 'taxoncode': '[Pll.fi/my]', 'taxonname': 'Polygonella fimbriata/P. myriophylla', 'author': '(Elliott) Horton, 1963|(Small) Horton, 1963', 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 10135, 'validatorid': 44, 'validatedate': datetime.date(2017, 10, 17), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2017, 10, 17, 15, 42, 41), 'count': 0})
  RealDictRow({'taxonid': 229, 'taxoncode': '[Pol.ud]', 'taxonname': 'Polygonum undiff.', 'author': 'Linnaeus, 1753', 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 3702, 'validatorid': 44, 'validatedate': datetime.date(2017, 10, 17), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2017, 10, 17, 3, 6, 4), 'count': 0})
  RealDictRow({'taxonid': 273, 'taxoncode': 'Slx.ve', 'taxonname': 'Salix vestita', 'author': 'Pursh, 1814[1813]', 'valid': True, 'highertaxonid': 271, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 3715, 'validatorid': 44, 'validatedate': datetime.date(2015, 1, 3), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2015, 1, 3, 16, 45, 57), 'count': 0})
  RealDictRow({'taxonid': 291, 'taxoncode': '[shrb.ud]', 'taxonname': 'Shrubs undiff.', 'author': None, 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': None, 'validatorid': 44, 'validatedate': datetime.date(2015, 1, 10), 'notes': None, 'recdatecreated': datetime.datetime(2013, 1, 1, 0, 0), 'recdatemodified': datetime.datetime(2015, 1, 10, 18, 40, 32), 'count': 0})
  RealDictRow({'taxonid': 303, 'taxoncode': '[tree.ud]', 'taxonname': 'Trees undiff.', 'author': None, 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': None, 'validatorid': 44, 'validatedate': datetime.date(2015, 1, 10), 'notes': None, 'recdatecreated': datetime.datetime(2013, 1, 1, 0, 0), 'recdatemodified': datetime.datetime(2015, 1, 10, 18, 48, 53), 'count': 0})
  RealDictRow({'taxonid': 333, 'taxoncode': 'Shr', 'taxonname': 'Schrankia', 'author': 'Willdenow, 1806', 'valid': True, 'highertaxonid': 29012, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 314, 'validatorid': 44, 'validatedate': datetime.date(2017, 3, 23), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2017, 3, 23, 14, 49, 36), 'count': 0})
  RealDictRow({'taxonid': 401, 'taxoncode': 'Ama.re-t', 'taxonname': 'Amaranthus retroflexus-type', 'author': 'Linnaeus, 1753', 'valid': True, 'highertaxonid': 5431, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 3658, 'validatorid': 44, 'validatedate': datetime.date(2017, 2, 7), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2017, 2, 7, 20, 10, 13), 'count': 0})
assert 17761 == 0
 +  where 17761 = len([RealDictRow({'taxonid': 183, 'taxoncode': '[Mimdae]', 'taxonname': 'Mimosoideae', 'author': 'de Candolle, 1825', 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 9757, 'validatorid': 44, 'validatedate': datetime.date(2020, 7, 27), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2020, 7, 27, 2, 4, 41), 'count': 0}), RealDictRow({'taxonid': 187, 'taxoncode': 'Bryida.ud', 'taxonname': 'Bryopsida undiff.', 'author': 'Pax, 1900', 'valid': True, 'highertaxonid': 659, 'extinct': False, 'taxagroupid': 'BRY', 'publicationid': 311, 'validatorid': 44, 'validatedate': datetime.date(2015, 1, 3), 'notes': None, 'recdatecreated': datetime.datetime(2013, 1, 1, 0, 0), 'recdatemodified': datetime.datetime(2015, 1, 3, 16, 55, 26), 'count': 0}), RealDictRow({'taxonid': 196, 'taxoncode': '[Osu.ud]', 'taxonname': 'Osmunda undiff.', 'author': 'Linnaeus, 1753', 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 9777, 'validatorid': 44, 'validatedate': datetime.date(2017, 4, 5), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recd... 1963|(Small) Horton, 1963', 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 10135, 'validatorid': 44, 'validatedate': datetime.date(2017, 10, 17), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2017, 10, 17, 15, 42, 41), 'count': 0}), RealDictRow({'taxonid': 229, 'taxoncode': '[Pol.ud]', 'taxonname': 'Polygonum undiff.', 'author': 'Linnaeus, 1753', 'valid': False, 'highertaxonid': None, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 3702, 'validatorid': 44, 'validatedate': datetime.date(2017, 10, 17), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2017, 10, 17, 3, 6, 4), 'count': 0}), RealDictRow({'taxonid': 273, 'taxoncode': 'Slx.ve', 'taxonname': 'Salix vestita', 'author': 'Pursh, 1814[1813]', 'valid': True, 'highertaxonid': 271, 'extinct': False, 'taxagroupid': 'VPL', 'publicationid': 3715, 'validatorid': 44, 'validatedate': datetime.date(2015, 1, 3), 'notes': None, 'recdatecreated': datetime.datetime(2012, 3, 21, 0, 0), 'recdatemodified': datetime.datetime(2015, 1, 3, 16, 45, 57), 'count': 0}), ...])

**Rationale**: If a taxon was entered into the database as a terminal leaf in the hierarchy, it ought to be associated with some data entry. If it is
absent from the variables table, then it was entered and never used.


**Remediation**:
- Check with data stewards for the particular data type.
- Ensure that the taxa are valid.


---

#### valid_005: sample_ages_scaled_properly

**Severity**: ERROR

**Description**: Sample ages and chronologies should have ages that have the correct age range. younger ages should always be more recent than older ages.

**Affected Tables**: `sampleages`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: sample_ages_scaled_properly (valid_005)
  Category: data_validity
  ================================================================================
  Description: Sample ages and chronologies should have ages that have the correct age range. younger ages should always be more recent than older ages.
  
  Rationale: The older and younger dates need to be ordered properly.
  
  Expected: No violations
  Found: 2 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'sampleageid': 138101, 'sampleid': 148850, 'chronologyid': 8389, 'age': None, 'ageyounger': 1970.0, 'ageolder': 1995.0, 'recdatecreated': datetime.datetime(2015, 5, 1, 1, 19, 22), 'recdatemodified': datetime.datetime(2015, 5, 1, 1, 19, 22)})
  RealDictRow({'sampleageid': 138102, 'sampleid': 148849, 'chronologyid': 8389, 'age': None, 'ageyounger': 1970.0, 'ageolder': 1995.0, 'recdatecreated': datetime.datetime(2015, 5, 1, 1, 19, 22), 'recdatemodified': datetime.datetime(2015, 5, 1, 1, 19, 22)})
assert 2 == 0
 +  where 2 = len([RealDictRow({'sampleageid': 138101, 'sampleid': 148850, 'chronologyid': 8389, 'age': None, 'ageyounger': 1970.0, 'ageolder': 1995.0, 'recdatecreated': datetime.datetime(2015, 5, 1, 1, 19, 22), 'recdatemodified': datetime.datetime(2015, 5, 1, 1, 19, 22)}), RealDictRow({'sampleageid': 138102, 'sampleid': 148849, 'chronologyid': 8389, 'age': None, 'ageyounger': 1970.0, 'ageolder': 1995.0, 'recdatecreated': datetime.datetime(2015, 5, 1, 1, 19, 22), 'recdatemodified': datetime.datetime(2015, 5, 1, 1, 19, 22)})])

**Rationale**: The older and younger dates need to be ordered properly.

**Remediation**:
- Likely we just need to flip the ages around from younger to older.
- The chronology may also need some examination.


---

#### valid_006: samples_per_analysisunit

**Severity**: WARNING

**Description**: Although some datasets may have multiple samples per analysis unit per dataset, we should generally expect that most analysis units have only one set of samples.

**Affected Tables**: `samples`, `datasets`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: samples_per_analysisunit (valid_006)
  Category: data_validity
  ================================================================================
  Description: Although some datasets may have multiple samples per analysis unit per dataset, we should generally expect that most analysis units have only one set of samples.
  
  Rationale: We definitely see duplicate samples within an analysis unit (and within a dataset), but we want to make sure that we're not seeing errors here. 
  This is set as a warning, and possibly we can work to improve the query a bit.
  
  
  Expected: No violations
  Found: 2996 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'array_agg': [1351, 1352], 'datasetid': 202, 'databasename': 'North American Pollen Database'})
  RealDictRow({'array_agg': [1346, 1347], 'datasetid': 202, 'databasename': 'North American Pollen Database'})
  RealDictRow({'array_agg': [1354, 1355], 'datasetid': 202, 'databasename': 'North American Pollen Database'})
  RealDictRow({'array_agg': [675985, 676028, 675974, 676031, 676027, 676035, 676033, 676036, 676030, 676029], 'datasetid': 61117, 'databasename': 'Neotoma'})
  RealDictRow({'array_agg': [116071, 116072], 'datasetid': 9566, 'databasename': 'FAUNMAP'})
  RealDictRow({'array_agg': [500963, 500966], 'datasetid': 50240, 'databasename': 'European Pollen Database'})
  RealDictRow({'array_agg': [676037, 676042, 676038, 676041, 676039, 676045, 676043, 676046, 676044, 676040], 'datasetid': 61117, 'databasename': 'Neotoma'})
  RealDictRow({'array_agg': [704752, 704753], 'datasetid': 66097, 'databasename': 'FAUNMAP'})
  RealDictRow({'array_agg': [117735, 117736, 117737, 117738], 'datasetid': 10006, 'databasename': 'FAUNMAP'})
  RealDictRow({'array_agg': [116633, 116634, 116635, 116636, 116637, 116638, 116639], 'datasetid': 9736, 'databasename': 'FAUNMAP'})
assert 2996 == 0
 +  where 2996 = len([RealDictRow({'array_agg': [1351, 1352], 'datasetid': 202, 'databasename': 'North American Pollen Database'}), RealDictRow({'array_agg': [1346, 1347], 'datasetid': 202, 'databasename': 'North American Pollen Database'}), RealDictRow({'array_agg': [1354, 1355], 'datasetid': 202, 'databasename': 'North American Pollen Database'}), RealDictRow({'array_agg': [675985, 676028, 675974, 676031, 676027, 676035, 676033, 676036, 676030, 676029], 'datasetid': 61117, 'databasename': 'Neotoma'}), RealDictRow({'array_agg': [116071, 116072], 'datasetid': 9566, 'databasename': 'FAUNMAP'}), RealDictRow({'array_agg': [500963, 500966], 'datasetid': 50240, 'databasename': 'European Pollen Database'}), ...])

**Rationale**: We definitely see duplicate samples within an analysis unit (and within a dataset), but we want to make sure that we're not seeing errors here. 
This is set as a warning, and possibly we can work to improve the query a bit.


**Remediation**:
- Check the dataset to see if the samples are legitimately multiple samples within a single dataset.
- Check with the original publication, or upload data steward.
- Potentially remove duplicate or empty samples if they exist.


---

### ✅ Passed Tests

- **valid_001**: coordinates_in_valid_range
- **valid_004**: sites_not_on_equator

## Business Rules

**Pass Rate**: 1/3

### ❌ Failed Tests

#### bix_002: taxonnames_are_not_duplicated_within_groups

**Severity**: ERROR

**Description**: Although different ecological groups may have similar taxon names (e.g., Abronia in reptiles, plants, protists and fungi), within groups the taxonomic name should be unique.


**Affected Tables**: `taxa`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: taxonnames_are_not_duplicated_within_groups (bix_002)
  Category: business_rules
  ================================================================================
  Description: Although different ecological groups may have similar taxon names (e.g., Abronia in reptiles, plants, protists and fungi), within groups the taxonomic name should be unique.
  
  
  Rationale: If the same name is entered multiple times within the taxonomic table for a particular taxonomic group, we can expect that there is likely some
  issue with conflicting hierarchies that needs to be resolved by the data stewardship team.
  
  
  Expected: No violations
  Found: 140 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'taxonname': 'Parasida mckittricki', 'taxagroupid': 'INS', 'count': 2})
  RealDictRow({'taxonname': 'Rhadine howdeni', 'taxagroupid': 'INS', 'count': 2})
  RealDictRow({'taxonname': 'Jussiaea', 'taxagroupid': 'VPL', 'count': 2})
  RealDictRow({'taxonname': 'Anchicera', 'taxagroupid': 'INS', 'count': 2})
  RealDictRow({'taxonname': 'Acacia seyal', 'taxagroupid': 'VPL', 'count': 2})
  RealDictRow({'taxonname': 'Epistrophe', 'taxagroupid': 'INS', 'count': 2})
  RealDictRow({'taxonname': 'Dictamnus', 'taxagroupid': 'VPL', 'count': 2})
  RealDictRow({'taxonname': 'Heliotropium-type', 'taxagroupid': 'VPL', 'count': 2})
  RealDictRow({'taxonname': 'Pilea-type', 'taxagroupid': 'VPL', 'count': 2})
  RealDictRow({'taxonname': 'Phyllanthus reticulatus-type', 'taxagroupid': 'VPL', 'count': 2})
assert 140 == 0
 +  where 140 = len([RealDictRow({'taxonname': 'Parasida mckittricki', 'taxagroupid': 'INS', 'count': 2}), RealDictRow({'taxonname': 'Rhadine howdeni', 'taxagroupid': 'INS', 'count': 2}), RealDictRow({'taxonname': 'Jussiaea', 'taxagroupid': 'VPL', 'count': 2}), RealDictRow({'taxonname': 'Anchicera', 'taxagroupid': 'INS', 'count': 2}), RealDictRow({'taxonname': 'Acacia seyal', 'taxagroupid': 'VPL', 'count': 2}), RealDictRow({'taxonname': 'Epistrophe', 'taxagroupid': 'INS', 'count': 2}), ...])

**Rationale**: If the same name is entered multiple times within the taxonomic table for a particular taxonomic group, we can expect that there is likely some
issue with conflicting hierarchies that needs to be resolved by the data stewardship team.


**Remediation**:
['Identify the `correct` entry, remove duplicate entries.']

---

#### bix_003: variable_elements_in_use

**Severity**: WARNING

**Description**: Over time a number of variable contexts, units and elements have been created but not neccessarily used. In some cases this may have resulted from improperly entered data 
in the Tilia spreadsheet.


**Affected Tables**: `variablecontexts`, `variableelements`, `variableunits`

**Error**: AssertionError: 
  ================================================================================
  Test Failed: variable_elements_in_use (bix_003)
  Category: business_rules
  ================================================================================
  Description: Over time a number of variable contexts, units and elements have been created but not neccessarily used. In some cases this may have resulted from improperly entered data 
  in the Tilia spreadsheet.
  
  
  Rationale: We want to ensure that the variables defined within the controlled vocabularies match with accepted external values, and that the variables that a user may
  select for data analysis are reflected in reality.
  
  
  Expected: No violations
  Found: 91 violations
  
  Sample violations:
  --------------------------------------------------------------------------------
  RealDictRow({'table': 'variablecontexts', 'identifier': 125, 'value': 'Pre-Quaternary'})
  RealDictRow({'table': 'variablecontexts', 'identifier': 133, 'value': 'corroded'})
  RealDictRow({'table': 'variableunits', 'identifier': 209, 'value': 'g/cm2/yr'})
  RealDictRow({'table': 'variableunits', 'identifier': 218, 'value': 'count of PCR replicates'})
  RealDictRow({'table': 'variableunits', 'identifier': 27, 'value': 'units not specified'})
  RealDictRow({'table': 'variableunits', 'identifier': 241, 'value': 'mmol/mol'})
  RealDictRow({'table': 'variableunits', 'identifier': 211, 'value': 'kg/m2/yr'})
  RealDictRow({'table': 'variableunits', 'identifier': 46, 'value': 'elemental ratio'})
  RealDictRow({'table': 'variableunits', 'identifier': 32, 'value': 'meq/L'})
  RealDictRow({'table': 'variableunits', 'identifier': 78, 'value': '1-2 scale'})
assert 91 == 0
 +  where 91 = len([RealDictRow({'table': 'variablecontexts', 'identifier': 125, 'value': 'Pre-Quaternary'}), RealDictRow({'table': 'variablecontexts', 'identifier': 133, 'value': 'corroded'}), RealDictRow({'table': 'variableunits', 'identifier': 209, 'value': 'g/cm2/yr'}), RealDictRow({'table': 'variableunits', 'identifier': 218, 'value': 'count of PCR replicates'}), RealDictRow({'table': 'variableunits', 'identifier': 27, 'value': 'units not specified'}), RealDictRow({'table': 'variableunits', 'identifier': 241, 'value': 'mmol/mol'}), ...])

**Rationale**: We want to ensure that the variables defined within the controlled vocabularies match with accepted external values, and that the variables that a user may
select for data analysis are reflected in reality.


**Remediation**:
- Where possible, remove unused units/elements/contexts - Ensure any near-duplicates of existing units/elements/contexts are using best-practice or accepted notations.


---

### ✅ Passed Tests

- **biz_001**: modern_samples_have_recent_dates


