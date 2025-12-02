# Connecting to Neotoma

## A Local Neotoma

If you have obtained a version of the Neotoma Database Snapshot from the web, you have a monthly snapshot of the database that can be used locally using a Postgres Database service.

To use the snapshot you must have [Postgres](https://www.postgresql.org/) installed on your computer. Postgres is a database system, a RDBMS (**R**elational **D**ata**B**ase **M**anagement **S**ystem).

### New to Databases?

An RDBMS is a bit different than other programs you might have run on your computer before. An RDBMS is really a tool to manage data access from your harddrive, to memory, to whatever program is using the data, whether that is an R script, Python, or some other program you want to use.

Some database-specific applications you may want to use include:

* PGAdmin4
* DBeaver
* DataGrip
* Postgres Plugin for VS Code

There is also a built-in commandline utility for Postgres that can be accessed from the commandline using `psql`.

When you set up the database server (by installing Postgres on your computer and ensuring that it is running in the background) you will likely have set up a user name and password. The defaults for postgres are:

* `username`: *postgres*
* `password`: *postgres*
* `database`: *postgres*
* `host`: *localhost*
* `port`: 5432

Whenever you connect to the Postgres server you will connect to it using the host, port, password and username.

## Local Connections in Multiple Languages

If you are connecting to the database locally, you will use your local database password/username.

### R

Several packages can be used to connect to a Postgres database using R. These include `dbply`, `RPostgreSQL` and `RPostgres`. Information about tables can be found in the [Database Table Overview][Database-Table-Overview].

```r
library(RPostgreSQL)
pcon <- dbConnect("Postgres",
                    user = "postgres",
                    password = "postgres",
                    host = "localhost",
                    dbname = "neotoma",
                    port = 5432)
res <- dbSendQuery(con, "SELECT * from ndb.sites LIMIT 10")
data <- fetch(res, n = -1)
```

### Python

Python programs developed by the Neotoma team generally use the `psycopg` or `psycopg2` Python libraries:

```python
import psycopg2
from psycopg2.extras import RealDictCursor

con = psycopg2.connect({"host":"localhost",
                        "port":5432,
                        "user":"postgres",
                        "password":"postgres",
                        "database":"neotoma"},
                        connect_timeout=5, cursor_factory=RealDictCursor)

query = """ SELECT *
                FROM ndb.taxa
                WHERE highertaxonid = %(taxonid)s
                AND NOT taxonid = highertaxonid
            """
    with con.cursor() as cur:
        _ = cur.execute(query, {'taxonid': 1})
        result = cur.fetchall()
```

### Javascript

The Neotoma API and Tilia APIs are written using JavaScript. The database connections with those scripts use the `pg-promise` library:

```JavaScript
const pgPromise = require('pg-promise');
const pgp = pgPromise();
const connection = pgp({"host":"localhost","port":5432,
                        "user":"postgres", "password":"postgres",
                        "database":"neotoma"})

result = db.any("SELECT * FROM ndb.sites LIMIT 10;")
        .then(function(data) {
          if (data.length === 0) {
          // We're returning the structure, but nothing inside it:
            var returner = [];
          } else {
            returner = data;
          };

          return returner;
        });
```

## Remote Connections

If you are an administrator for Neotoma you will have a unique password and username tied to your role in the organization. You will also be required to use an SSH Tunnel into the database server to ensure added security. Because of the way Neotoma is structured on AWS, all administrative users must let the Administrator know what IP address they will be logging into with. They must also use their own ssh client to tunnel into the database server. This is all explained elsewhere.

Regardless, connecting remotely means that users will chane their `port`, `host`, `username` and `password` to match the new values.
