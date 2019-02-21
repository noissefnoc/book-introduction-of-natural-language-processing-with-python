#!/usr/bin/env python

import json
import sqlite3

conn = None


def connect():
    global conn
    conn = sqlite3.connect('./sample.db')


def close():
    conn.close()


def create_table():
    conn.execute('DROP TABLE IF EXISTS docs')
    conn.execute("CREATE TABLE docs (\n"
                 "            id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                 "            content   TEXT,\n"
                 "            meta_info BLOB,\n"
                 "            sentence  BLOB,\n"
                 "            chunk     BLOB,\n"
                 "            token     BLOB\n"
                 "        )")


def load(values):
    conn.executemany(
        'INSERT INTO docs(content, meta_info) VALUES (?, ?)',
        values)
    conn.commit()


def get(doc_id, fl):
    row_ls = conn.execute(
        'SELECT {} FROM docs WHERE id = ?'.format(','.join(fl)),
        (doc_id,)).fetchone()
    row_dict = {}
    for key, value in zip(fl, row_ls):
        row_dict[key] = value
    return row_dict


def get_all_ids(limit, offset=0):
    return [record[0] for record in
            conn.execute(
                'SELECT id FROM docs LIMIT ? OFFSET ?',
                (limit, offset))]
