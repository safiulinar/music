import sqlite3

conn = sqlite3.connect('music.db')

cur = conn.cursor()
cur.execute("""select * from artist;
            """)

print(cur.fetchall())