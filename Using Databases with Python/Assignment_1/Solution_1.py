# Author : Abhishek Katyare
# Date   : 25th October, 2019

import sqlite3

conn = sqlite3.connect("solutiondb.sqlite")
cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS Ages
''')

cur.execute('''
    CREATE TABLE Ages ( 
    name VARCHAR(128), 
    age INTEGER
    )
''')

cur.execute('''
    DELETE FROM Ages;
''')

cur.execute('''
    INSERT INTO Ages (name, age) VALUES ('Toluwanimi', 25);
''')

cur.execute('''
    INSERT INTO Ages (name, age) VALUES ('Alessio', 22);
''')

cur.execute('''
    INSERT INTO Ages (name, age) VALUES ('Patrycja', 17);
''')

cur.execute('''
    INSERT INTO Ages (name, age) VALUES ('Avani', 25);
''')

cur.execute('''
    SELECT * FROM Ages;
''')
data = cur.fetchall()

for row in data:
    print(row)


cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
print(cur.fetchall())
