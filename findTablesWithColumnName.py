#!/usr/bin/env python3

import sys
import sqlite3

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <sqlite_db> <column_name>")
    sys.exit(1)

bookmarks_db = sys.argv[1]
column_name = sys.argv[2]

conn = sqlite3.connect(bookmarks_db)

tables = conn.execute(f'''
SELECT 
    m.name AS table_name,
    p.name AS column_name
FROM 
    sqlite_master AS m
JOIN 
    pragma_table_info(m.name) AS p
WHERE 
    p.name = '{column_name}'
ORDER BY 
    m.name;
''').fetchall()

print(f"Tables with '{column_name}' column:")
for i in tables:
    print(i[0])

conn.close()

