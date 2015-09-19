#!/usr/bin/env python
import sqlite3

def connect():
    conn = sqlite3.connect("web.db")
    c = conn.cursor()
    return (conn, c)

def isTableExists((conn, cursor), tableName):
    try:
        conn.execute("SELECT * from %s" % tableName)
        return True
    except:
        return False
#column
def isTableColumnExists((conn, cursor), tableName, column):
    try:
        conn.execute("SELECT %s from %s" % (column ,tableName))
        return True
    except:
        return False

def exeDB((conn, cursor), query):
    rows = []
    try:
        cursor.execute(query)
        conn.commit()
        rows = cursor.fetchall()
    except:
        raise ValueError("exeDB error")

    return rows
