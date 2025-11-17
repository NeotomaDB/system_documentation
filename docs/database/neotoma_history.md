# History of the Constituent Databases

## Global Pollen Database

In an early effort, the Cooperative Holocene Mapping Project [@Members1988;@Wright1993c] assembled pollen data in the 1970s and 1980s to test climate models. Although data-model comparison was the principal objective of the COHMAP project, the  synoptic analyses of the pollen data, particularly maps showing the constantly shifting ranges of species in response to climate change, were revelatory and led to much ecological insight [e.g. @Webb1981;@Webb1987a;@Webb1988b].

The COHMAP pollen "database" was a set of flat files with a fixed file format for data and for chronologies. FORTRAN programs were written to read these files and to assemble data for particular analyses. Thompson Webb III managed the COHMAP pollen database at Brown University, but as the quantity of data increased, data management became increasingly cumbersome; the data needed to be migrated to a relational database management system. Discussions with E. C. Grimm led to the initiation of the North American Pollen Database (NAPD) in 1990.

At the same time in , the International Geological Correlation Project IGCP 158 [@Church1989IGCPP1] was conducting a major collaborative synthesis of paleoecological data, primarily of pollen, making the need for a pollen database painfully obvious. In the forward to the book resulting from this project [@berglund1996palaeoecological], J.L. de Beaulieu describes the role that the IGCP 158 project had in launching the European Pollen Database [@Huntley1993b]. A workshop to develop a European Pollen Database (EPD) was held in in 1. North American representatives also attended, and the organizers of NAPD and EPD commenced a long-standing collaboration to develop compatible databases. NAPD and EPD held several joint workshops and developed the same data structure. Nevertheless, the two databases were independently established, partly because Internet capabilities were not yet sufficient to easily manage a merged database. The pollen databases were developed in Paradox, which at the time was the most powerful RDBMS readily available for the PC platform. NAPD and EPD established two important protocols:

* the databases were relational and queryable
* they were publicly available.

As the success the NAPD-EPD partnership escalated, working groups initiated pollen databases for other regions, including the Latin American Pollen Database (LAPD) in 1994 [ultimately @Flantua2015-lo], the Pollen Database for and the Russian Far East (PDSRFE) in 1995, and the African Pollen Database (APD) in 1996 [@Lezine2021-wd]. At its initial organizational workshop, LAPD opted to merge with NAPD, rather than develop a standalone database, and the Global Pollen Database was born. PDSRFE also followed this model. APD developed independently, but uses the table structure of GPD and EPD. Pollen database projects have also been initiated in other regions, and the GPD contains some of these data, including the Indo-Pacific Pollen Database [@Herbert2024-bq] and the Japanese Pollen Database.

```{sql, ageSamples, connection=db, output.var="sampleroundcount", echo=FALSE}
SELECT ROUND(age::bigint, -2) AS age, COUNT(*) AS n
FROM ndb.sampleages
WHERE age IS NOT NULL
GROUP BY ROUND(age::bigint, -2);
```

```{r, agedistributions, echo=FALSE, fig.alt="Histogram of sample age distributions in Neotoma for the first 200000 years of samples showing that data is heavily skewed the the present.", fig.cap="Sample age distributions in Neotoma for a subset of Neotoma data.  Ages are heavily skewed to samples in the last 10,000 years, and moreso to the near-present.", warnings=FALSE}
ggplot(sampleroundcount, aes(x = age, y = n)) +
    geom_histogram(stat="identity", width=500) +
    scale_x_continuous() +
    theme_bw() +
    xlab('Years Before Present') +
    ylab('Age Count')
```

The pollen databases contain data from the Holocene, Pleistocene, and Pliocene, although most data are from the last 20,000 years (Fig. \@ref(fig:agedistributions)). Included are fossil data, mainly from cores and sections, and modern surface samples, which are essential for calibrating fossil data. NAPD data are not separate from the GPD, but rather the NAPD is the North American subset of GPD. EPD has both public and restricted data -- a concession that had to be made early on to assuage some contributors.

## North American Plant Macrofossil Database

Plant macrofossils include plant organs generally visible to the naked eye, including seeds, fruits, leaves, needles, wood, bud scales, and megaspores. Synoptic-scale mapping of plant macrofossils from modern assemblages [@Jackson1997] and fossil assemblages [@Jackson1997;@Jackson2000c;@Jackson2002] have shown the utility of plant macrofossils in providing spatially and taxonomically precise reconstructions of past species ranges. Although plant macrofossil records are spatially precise, synoptic networks of high-quality sites can scale up to yield aggregate views of past distributions [@Jackson1997]. In addition, macrofossils, with their greater taxonomic resolution, augment the pollen data by providing information on which species might have been present, and can resolve issues of long-distance transport [@Birks2003].

The North American Plant Macrofossil Database (NAPMD) has been directed by S.T. Jackson at the . Highest priority has been placed on data from the last 30,000 years, although some earlier Pleistocene and late Pliocene data are included. The database originated as a research database for selected taxa from Late Quaternary sediments of eastern North America [@Jackson1997]. In 1994, an effort was initiated with NOAA funding to build on this foundation to develop a cooperative, relational database comprising all of , a longer time span, and all plant taxa.

The structure of NAPMD was adapted from the pollen database and was also stored in a Paradox file format. Although the plant macrofossil database was well served by the data model structure, modifications were made to accommodate different organs from the same species and to deal with the various quantitative measures of abundance. The Plant Macrofossil database also included surface samples, which were not part of the pollen databases at the time, but are useful for the interpretation of fossil data.

## FAUNMAP

R.W. Graham, E.L. Lundelius, Jr., and a group of Regional Collaborators organized a project to develop a database for late Quaternary faunal data from the , which the U.S. NSF funded in 1990. This project had a research agenda, and its seminal paper focused on the individualistic behavior displayed by animal species [@Group1994].

Two FAUNMAP databases exist, FAUNMAP I and FAUNMAP II. Both databases were coordinated by R. W. Graham and E. L. Lundelius, Jr. and funded by NSF. Both are relational databases for fossil mammal sites. The data were extracted from peer-reviewed literature, selected theses and dissertations, and selected contract reports for both paleontology and archaeology (all data is currently contained within the Neotoma publications tables). Unpublished collections were not included. Data were originally captured in Paradox but were later migrated to Microsoft Access.

FAUNMAP I contains data from sites in the continental United States (the lower 48 States) that date between 500 BP and \~40,000 BP. Funding for FAUNMAP I ended in 1994, with the production of two major publications by the FAUNMAP Working Group [@Group1994;@Group1996], along with publications from individual members and many others who accessed the database on-line. Graham and Lundelius continued the FAUNMAP project, developing FAUNMAP II with funding from NSF beginning in 1998. FAUNMAP II [@faunmapTwo] shares the same structure as FAUNMAP I but expands the spatial coverage to include and and extends the temporal coverage to the Pliocene (5 Ma). In addition, sites published since 1994, when FAUNMAP I was completed, have been added for the contiguous 48 States. In all, FAUNMAP I and II contain more than 5000 fossil-mammal sites with more than 600 mammal species for all of North America north of Mexico that range in age from 0.5 ka to 5 Ma­.

The detailed structure of the FAUNMAP database is described in FAUNMAP Working Group [@Group1994]. Sites identified by name and location were subdivided into Analysis Units (AU's), which varied from site to site depending upon the definitions used in the original publications (e.g., stratigraphic horizons, cultural horizons, excavation levels, biostratigraphic zones). All data (*i.e.*, taxa identified, and counts of individual specimens) and metadata (sediment types, depositional environments, facies, radiometric and other geochronological dates, modifications of bone) were associated with the individual AUs. This structure -- analysis units within sites -- allows for information to be extracts at the site level, or at the smallest sample subdivision. The analysis unit permits fine-scale temporal resolution and analysis. Similar to the GPD and NAPMD, FAUNMAP contains archival and research tables. Similar to the plant macrofossil database, FAUNMAP contains a variety of quantitative measures of abundance (*e.g.*, MNI, NISP), and presence data are more commonly used for analysis.

## BEETLE

Many beetles have highly specific ecological and climatic requirements and are valuable indicators of past environments [@morgan1983late;@ashworth2001aapg;@ashworth2004coleoptera]. Coleoptera is one of the most diverse groups of organisms on Earth, and of the insects, perhaps the most commonly preserved as fossils. Allan Ashworth has assembled a database of fossil beetles from . The data, which were recorded in Excel, contain 5523 individual records of 2567 taxa from 199 sites and 165 publications. Metadata include site name, latitude and longitude, lithology of sediment, absolute age, and geological age. The basic data are similar to plant and mammal databases -- lists of taxa from sites. The metadata have not been recorded to the extent of the other databases, especially chronological data, but Ashworth has resolved the taxonomic issues and has assembled the publications, so that the additional metadata can be easily pulled together.
