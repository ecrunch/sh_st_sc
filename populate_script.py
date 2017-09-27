import csv
import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS test""")
cur.execute("""CREATE TABLE test
            (taco text, flavor text, kisses text)""")
cur.execute("""INSERT INTO test VALUES (taco,flavor,kisses)""","test")
conn.commit()
conn.close()
