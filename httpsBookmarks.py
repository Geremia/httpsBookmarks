#!/usr/bin/env python3

import sys
import sqlite3

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <places.sqlite in Firefox profile dir>")
    sys.exit(1)

bookmarks_db = sys.argv[1]

conn = sqlite3.connect(bookmarks_db)

conn.execute('''
UPDATE moz_places
SET url = REPLACE(url, 'http://', 'https://')
WHERE url LIKE 'http://%';
''')
result = conn.execute('''
UPDATE moz_places
SET url = REPLACE(url, 'https://localhost', 'http://localhost')
WHERE url LIKE 'https://%';
''')
print(f"Made sure {result.rowcount} bookmarks (sans localhost ones) are HTTPS.")

conn.commit()
conn.close()

