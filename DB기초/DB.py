import sqlite3

con = sqlite3.connect("kospi.db") #kospi.db와 연결 없으면 새로 생성
                                  #con은 connection객체
cursor = con.cursor() #DB파일에 데이터를 입력하기 위해서 cursor객체 생성필요
#cursor.execute("CREATE TABLE kospi(Name text, ClosingPrice int)") #테이블생성
cursor.execute("INSERT INTO kospi VALUES('LG전자', 74500)")
cursor.execute("INSERT INTO kospi VALUES('네이버', 774000)")
cursor.execute("INSERT INTO kospi VALUES('다음', 169100)")
con.commit() #작업내용 DB에 반영하기 위해서 커밋
con.close #DB닫기

#DB에서 데이터 읽기
#con = sqlite3.connect("kospi.db")
#cursor = con.cursor()
cursor.execute("SELECT * FROM kospi")
for row in cursor:
    print(row)

#cursor.fetchall()
