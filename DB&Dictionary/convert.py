import sqlite3
import json                            #json모듈 import
#import nclDBInsert                     #NCL.db만들기

connection = sqlite3.connect("NCL.db") #db연결
cursor = connection.cursor()           #cursor연결
cursor.execute("select * from NCL")    #select문 수행
result = cursor.fetchall()            #모든 내용 가져오기

#json형태의 객체를 만들기 위한 dumps, loads과정
a = json.dumps(result[0][0])
wonikName=json.loads(a)
a = json.dumps(result[0][1])
wonikPhone=json.loads(a)
a = json.dumps(result[0][2])
wonikEmail=json.loads(a)
a = json.dumps(result[0][3])
wonikAge=json.loads(a)

a = json.dumps(result[1][0])
sukwonName=json.loads(a)
a = json.dumps(result[1][1])
sukwonPhone=json.loads(a)
a = json.dumps(result[1][2])
sukwonEmail=json.loads(a)
a = json.dumps(result[1][3])
sukwonAge=json.loads(a)

a = json.dumps(result[2][0])
haewonName=json.loads(a)
a = json.dumps(result[2][1])
haewonPhone=json.loads(a)
a = json.dumps(result[2][2])
haewonEmail=json.loads(a)
a = json.dumps(result[2][3])
haewonAge=json.loads(a)

#key, value값을 가진 dictionary화 시키기
wonik={'Name':wonikName, 'Phone':wonikPhone, 'Email':wonikEmail, 'Age':wonikAge}
sukwon={'Name':sukwonName, 'Phone':sukwonPhone, 'Email':sukwonEmail, 'Age':sukwonAge}
haewon={'Name':haewonName, 'Phone':haewonPhone, 'Email':haewonEmail, 'Age':haewonAge}
