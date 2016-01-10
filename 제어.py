#제어

#예제4.1 학점계산
>>>score = int(input(('Input Score : '))) #사용자로부터 값 입력받음
Input score: 80
>>> if 90 <= score <100:
	grade = "A"
elif 80 <= score <90:
	grade = "B"
elif 70 <= score <80:
	grade = "C"
elif 60 <= score <70:
	grade = "D"
else:
	grade = "F"

#들여쓰기 주의!!
	
>>> print("Grade is " + grade)
Grade is B

=============================== RESTART: Shell ===============================
>>> #for문
>>> l = ['Apple', 100, 15.23]
>>> for i in l:
	print(i, type(i))

	
Apple <class 'str'>
100 <class 'int'>
15.23 <class 'float'>
>>> 
>>> 
>>> d = {"Apple":100, "Orange":200, "Banana":300}
>>> for k, v in d.items(): #사전 출력
	print(k,v)

	
Banana 300
Orange 200
Apple 100

#구구단 출력
>>> for n in [1,2]:
	print("--{0} 단 --".format(n)) #{0}은 숫자임
	for i in [1,2,3,4,5,6,7,8,9]:
		print("{0} * {1} = {2}".format(n,i,n*i))

		
--1 단 --
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
--2 단 --
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
=============================== RESTART: Shell ===============================
>>> #수열생성 range()
>>> list(range(10)) #종료 값만 있는 경우-10은 포함되지않음
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(10, 0 ,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> #리스트 항목과 인덱스 값 동시에 얻기 enumerate()
>>> L = [100, 15.5, "Apple"]
>>> for i in enumerate(L):
	print(i)

	
(0, 100)
(1, 15.5)
(2, 'Apple')
>>> for i, v in enumerate(L, 101):
	print(i,v)

	
101 100
102 15.5
103 Apple
>>> # 앞의 값은 인덱스 값임


>>> #리스트 내장
>>> ㅣ = [1,2,3,4,5]
>>> [i**2 for i in l]
[1, 4, 9, 16, 25]
>>> t=('apple','banana','orange') #튜플객체
>>> [len(i) for i in t] #각 문자열의 길이를 리스트로 반환
[5, 6, 6]
>>> d = {100:'apple', 200:'banana', 300:'orange'} #사전객체
>>> [v.upper() for v in d.values()] #사전 문자열 대문자로 표시
['BANANA', 'ORANGE', 'APPLE']
>>> 
>>> l = ['apple', 'banana', 'orange', 'kiwi']
>>> [i for i in l if len(i) >5]
['banana', 'orange']

