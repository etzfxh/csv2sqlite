# csv2sqlite

Create an SQLite database from a collection of CSV files.

# Get started

Clone this repository. Then add the following line to your `~/.bashrc`:

```bash
# Adjust the script path as necessary!
alias csv2sqlite="python3 .../csv2sqlite/src/csv2sqlite.py"
```

# Requirements

Just a current `Python3` interpreter. There are no third party dependencies.

# Usage

The default case is as easy as:

```bash
$ cd directory/containing/csv/files
$ csv2sqlite
```

The default case is illustrated by the `test` directory:

```bash
$ ls -1 test
authors_books.csv
authors.csv
books.csv
schema.sql
```

- The CSV files are all in the same directory.
- There is an explicit `schema.sql` in that same directory.
- The SQLite database does not exist yet.
- Executing `$ cd test && csv2sqlite` will create a database `test/test.sqlite`, i.e. in the same directory, named after the directory, with the file extension `.sqlite`.

Future releases shall provide command line options for additional use cases:

- CSV files in different places than the working directory.
- Custom database path.
- Overwrite or extend an existing database.
- Custom schema path or no explicit schema at all.

# Correspondence between schema and CSV files

When there is an explicit schema, the following assumptions are made:

- For each CSV file, the schema contains a table with the same name. Example: For a CSV file `books.csv` there is a database table `books`.
- The first row of each CSV file contains the column names, and each CSV column name is a field name in the corresponding database table (in arbitrary order).
- The CSV data does not violate any database constraints (e.g. NOT NULL, UNIQUE).
