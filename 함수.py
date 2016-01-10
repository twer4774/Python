#함수

#기본문법
def Times(a,b):
    return a*b
=============================== RESTART: Shell ===============================
>>> #두개의 리스트에서 교집합 구하기
>>> def intersect(prelist, postlist):
	retList = []
	for x in prelist:
		if x in postlist and x  not in retList:
			retList.append(x)
			return retList

		
>>> list1="SPAM"
>>> list2="EGG"
>>> intersect(list1, list2)
>>> #빈 리스트가 출력된것
>>> 
>>> intersect(list1, ['H', 'A', 'M'])
['A']
>>> #왜 M은 출력되지 않는지??
>>> 
>>> tup1=('B','E','E','F')
>>> intersect(list2, tup1) #혼합자료형
['E']

=============================== RESTART: Shell ===============================
>>> #인자전달 - 변경가능한 변수
>>> def change(x):
	x[0] = 'H'

	
>>> wordlist['J','A','M']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    wordlist['J','A','M']
NameError: name 'wordlist' is not defined
>>> wordlist = ['J','A','M']
>>> change(wordlist)
>>> wordlist
['H', 'A', 'M']
>>> 
=============================== RESTART: Shell ===============================
>>> def testGlobal(a):
	global g
	return g +a

>>> testGlobal(1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    testGlobal(1)
  File "<pyshell#12>", line 3, in testGlobal
    return g +a
NameError: name 'g' is not defined

>>> g = 2
>>> testGlobal(1)
3
>>> 
=============================== RESTART: Shell ===============================
>>> #함수인자
>>> #기본 인자값
>>> def Times(a=10, b=20):
	return 1*b

>>> Times()
20
>>> def Times(a=10, b=20):
	return a*b

>>> Times()
200
>>> Times(5) #a에만 5가 할당됨
100
>>> 
>>> #키워드 인자
>>> def connectURI(server, port):
	str="http://"+server+":"+port
	return str

>>> connectURI("test.com","8080")
'http://test.com:8080'

>>> conncetURI(port="8080", server="test.com")#명시적 인자이름사용

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    conncetURI(port="8080", server="test.com")#명시적 인자이름사용
NameError: name 'conncetURI' is not defined

>>> connectURI(port="8080", server="test.com") #명시적 인자이름 사용
'http://test.com:8080'

>>> #lambda(람다)함수
>>> g = lambda x, y:x*y
>>> g(2,3)
6
>>> (lambda x: x*x)(3)
9
>>> g(2,5)
10
>>> #(lambda x:x*x)(3)의 함수객체는 사용뒤 바로 사라짐
