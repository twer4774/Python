import json
import sqlite3

con = sqlite3.connect("NCL.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE ncl(Name text, Phone text, Email text, Age int)")
cursor.execute("INSERT INTO ncl VALUES('wonik', '010-4194-4774', 'twer4774@gmail.com', 25)")
cursor.execute("INSERT INTO ncl VALUES('sukwon', '010-7184-6634', 'dudtntdud@gmail.com', '24')")
cursor.execute("INSERT INTO ncl VALUES('haewon', '010-2339-9117', 'alxh7895@naver.com', '22')")
con.commit()
con.close()


