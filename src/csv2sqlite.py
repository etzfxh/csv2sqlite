#!/usr/bin/python3

import csv
from datetime import datetime as dt
import os
import pathlib
import sqlite3
import sys

SCHEMA_FNAME = 'schema.sql'
DB_FNAME_EXTENSION = '.sqlite'
CSV_FNAME_EXTENSION = '.csv'

def init_db(schema_path, db_path, verbose=False):
    if verbose:
        print(dt.now(), 'Init database: %s -> %s.' % (schema_path, db_path))
    with open(schema_path) as f:
        sql = f.read()
    db_connection = sqlite3.connect(db_path)
    db_connection.executescript(sql)
    db_connection.close()

def import_table(csv_path, db_path, verbose=False):
    '''
    TODO: Take care of quoting inside the CSV file.
    '''
    if verbose:
        print(dt.now(), 'Import table: %s -> %s.' % (csv_path, db_path))
    with open(csv_path) as csv_file:
        reader = csv.DictReader(csv_file)
        column_names_joined = ','.join(reader.fieldnames)
        placeholders_joined = ','.join(['?' for _ in reader.fieldnames])
        table_name = pathlib.Path(csv_path).stem
        sql = 'INSERT INTO %s (%s) VALUES (%s);' % (
            table_name,
            column_names_joined,
            placeholders_joined)
        db_connection = sqlite3.connect(db_path)
        cursor = db_connection.cursor()
        cursor.executemany(sql, [tuple(row.values()) for row in reader])
        db_connection.commit()
        db_connection.close()

def csv2sqlite(db_directory=None, csv_directory=None, verbose=False):
    working_directory = os.getcwd()
    db_directory = db_directory or working_directory
    csv_directory = csv_directory or working_directory

    db_name = os.path.basename(db_directory)
    db_path = os.path.join(db_directory, db_name + DB_FNAME_EXTENSION)
    assert not os.path.exists(db_path), 'Database exists already: %s' % db_path

    schema_path = os.path.join(csv_directory, SCHEMA_FNAME)
    assert os.path.isfile(schema_path), 'Schema not found: %s' % schema_path

    csv_fnames = sorted([
        fname for fname in os.listdir(csv_directory)
        if fname.endswith(CSV_FNAME_EXTENSION)])
    csv_paths = [os.path.join(csv_directory, fname) for fname in csv_fnames]

    init_db(schema_path, db_path, verbose=verbose)
    for csv_path in csv_paths:
        import_table(csv_path, db_path, verbose=verbose)

def main():
    '''
    TODO: Currently, this function is just an alias for csv2sqlite(). Its
        purpose is eventually to contain logistics for command line options.
    '''
    csv2sqlite()

def test():
    csv2sqlite(verbose=True)

if __name__ == '__main__':
    main()
#    test()
