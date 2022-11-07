# main

import sqlite3 as sql

def establish_connection(database_name):
    conn = sql.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor
