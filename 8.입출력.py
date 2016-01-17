#입출력

>>> import sys
>>> print("welcome to", "python", sep="~", end="!", file=sys.stderr)
welcome to~python!
>>> f = open('test.txt', 'w')
>>> print("file write", file=f)
>>> f.close()

=============================== RESTART: Shell ===============================
>>> for x in range(1,6):
	print(x,'x',x,'=',x*x)

	
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
=============================== RESTART: Shell ===============================
>>> #제곱의 결과 오른쪽 정렬 rjust(v) v가 최대수보다 커야됨.
#ljust왼, center가운데, zfill(v)하면 v만큼 0채움 
>>> for x in range(1,6):
	print(x,'x',x,'=',str(x*x).rjust(3))

	
1 x 1 =   1
2 x 2 =   4
3 x 3 =   9
4 x 4 =  16
=============================== RESTART: Shell ===============================
>>> #포맷팅 format()메서드
>>> print("{0} is {1}".format("apple","red"))
apple is red
>>> print("{item} is {color}".format(item="apple", color="red"))
apple is red
>>> dic={"item":"apple", "color":"red"}
>>> print("{0[item]} is {0[color]}".format(dic))
apple is red
>>> 
>>> item = "apple"
>>> color = "red"
>>> print("{0[item]} is {0[color]}".format(locals())) #지역변수들을 사전형식으로 변환하는 함수 - locals()이용
apple is red
>>> #**기호 사용시 {0[item]} 인덱스 0 제거 가능
>>> print("{item} is {color}".format(**locals()))
apple is red
>>> print("{item} is {color}".format(**dic))
apple is red
=============================== RESTART: Shell ===============================
>>> #입력
>>> a = input('insert any keys:')
insert any keys:test
>>> print(a)
test
=============================== RESTART: Shell ===============================
>>> #파일 입출력
>>> f = open('test.txt', 'w')
>>> f.write('plow deep\nwhile sluggards sleep')
31 #몇바이트나 썼는지
>>> f.close()

>>> #파일 내용 출력
>>> f = open('text.txt')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    f = open('text.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
>>> f = open('test.txt')
>>> f.read()
'plow deep\nwhile sluggards sleep'
>>> f.close()
>>> f.closed
True
=============================== RESTART: Shell ===============================
>>> #음악파일 복사하기 경로는 python에 있어야함
>>> f = open('Kalimba2.mp3', 'wb')
>>> f.write(open('Kalimba.mp3', 'rb').read())
8414449
>>> f.close()
>>> f.closed
True
=============================== RESTART: Shell ===============================
>>> #파일 줄단위 읽기
>>> f = open('test.txt')
>>> f.read()
'plow deep\nwhile sluggards sleep'
>>> f.read()
''
>>> f.tell() #어디까지 읽었나확인
32 
>>> f.seek(0) #처음으로 돌아가기
0
>>> f.read() #처음부터 다시읽음
'plow deep\nwhile sluggards sleep'
>>> f.seek(0)
0
>>> f.readline() #줄단위로 읽기
'plow deep\n'
>>> f.readline()
'while sluggards sleep'
>>> f.readline()
''
>>> f.seek(0)
0
>>> f.readlines() #줄단위로 모두 리스트로 읽어옴
['plow deep\n', 'while sluggards sleep']
>>> f.readlines()
[]
>>> f.close()
=============================== RESTART: Shell ===============================
>>> #with 함수를 쓰면 close안해도 블록 벗어나면 알아서 파일닫아줌
>>> with open('test.txt') as f:
	print(f.readlines())
	print(f.closed)

	
['plow deep\n', 'while sluggards sleep']
False
>>> f.closed
True
>>> 
