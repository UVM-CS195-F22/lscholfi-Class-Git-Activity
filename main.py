# main

import sqlite3 as sql
import sys

def establish_connection(database_name):
    conn = sql.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor

def do_query(cursor, table_name, column_name):
    data = cursor.execute(f'''SELECT '{column_name}' FROM '{table_name}';''').fetchall()
    formated_data = ""
    for x in data:
        formated_data += x
        formated_data += '\n'

def main():
    args = sys.argv
    database_filename = args[1]
    table_name = args[2]
    column_name = args[3]
    conn, cursor = establish_connection(database_filename)
    do_query(cursor, table_name, column_name)
