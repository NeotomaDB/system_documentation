# Acknowledgements

The documentation for the [Neotoma Paleoecology Database](https://neotomadb.org) would not be possible without the extrordinary work of Dr. Eric C. Grimm [@Jacobson2021] who spent countless hours developing the original database manual, and was the center of an incredible community built around the database. Neotoma rests on the work of a number of researchers who contributed to the original North American Pollen Database, and subsequent data contributors, including FAUNMAP contributors and the data contributions of Allan Ashworth. The Neotoma Database would not exist were it not for the ongoing contributions of authors, data analysts and funding agencies, in particular the National Sciences Foundation. This manual draws heavily from Eric Grimm's original Neotoma manual (v2), published as [@Grimm2008a].

The Postgres snapshot of the database is accessible from [the Neotoma Snapshots page](http://www.neotomadb.org/snapshots). For users who may be interested in loading the database using Docker, a GitHub repository is available to install the latest snapshot and build a container locally.

This documentation is divided up to provide an overview of the core Neotoma Services. These include:

## Overview

* Database Documentation, which covers the major design concepts, table descriptions and examples of table use and vocabulary terms.
* API Documentation, the high-level method for accessing Neotoma data over the internet. The API (Application-Program Interface) uses URL queries to access information about Neotoma sites, datasets and more.
* AWS Cloud Infrastructure, providing standard operating procedures for data administrators, and providing guidance for researcher interested in how Neotoma has implemented its online design.
* R Documentation, providing guidance for the `neotoma2` R package.
* Workbooks, providing worked examples of Neotoma data workflows used by researchers.

## Contributing to Documentation

All documentation for Neotoma is managed in the Neotoma `system_documentation` GitHub repository. Most of the documentaiton is written using plain-text Markdown, in an effort to make editing and contributing documentation as simple as possible. All contributors are expected to follow the Contributor Code of Conduct. For more information please reach out.
