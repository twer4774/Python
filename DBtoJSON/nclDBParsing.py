import json
import sqlite3

con = sqlite3.connect("NCL.db")
cursor = con.cursor()

#cursor.execute("CREATE TABLE ncl(Name text, Phone text, Email text, Age int)")
cursor.execute("INSERT INTO ncl VALUES('wonik', '010-4194-4774', 'twer4774@gmail.com', 25)")
cursor.execute("INSERT INTO ncl VALUES('sukwon', '010-7184-6634', 'dudtntdud@gmail.com', '24')")
cursor.execute("INSERT INTO ncl VALUES('haewon', '010-2339-9117', 'alxh7895@naver.com', '22')")
con.commit()
con.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect("NCL.db")
connection.row_factory = dict_factory

cursor = connection.cursor()
cursor.execute("SELECT * FROM NCL")

results = cursor.fetchall()

print(results)

connection.close()
