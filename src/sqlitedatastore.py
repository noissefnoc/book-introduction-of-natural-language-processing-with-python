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
