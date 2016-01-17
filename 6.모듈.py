#모듈

>>> import math #math 모듈을 가져옴
>>> math.pow(2,10)
1024.0
>>> math.log(100)
4.605170185988092
>>> math.pi
3.141592653589793
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> 
=============================== RESTART: Shell ===============================
>>> #FTP서버에 접근하여 파일리스트 가져오는 프로그램
>>> from ftplib import FTP #ftplib 모듈에서 FTP클래스를 가져옴
>>> ftp = FTP("ftp1.at.proftpd.org") #ftp서버에 접속
>>> ftp.login() #로그인. login함수에 아무것도 적지않으면 anonymous로접속
'230 Anonymous access granted, restrictions apply'
>>> ftp.retrlines('LIST') #List를 가져옴
-rw-rw-r--   1 ftp      ftp           451 Jul  1  2005 README.MIRRORS
drwxrwxr-x   3 ftp      ftp          4096 Jul  1  2005 devel
drwxrwxr-x   3 ftp      ftp          4096 Dec  2  2010 distrib
drwxrwxr-x   4 ftp      ftp          4096 Jul  1  2005 historic
'226 Transfer complete'
>>> ftp.quit()
'221 Goodbye.'
=============================== RESTART: Shell ===============================
>>> #예제 simpleset.py 교,합,차집합 모듈
>>> #c:\python\lib에 저장 >>>없어야됨!!! 저장경로는 환경변수에서 바꿈
from functools import * #reduce 함수를 사용하기 위해 functools 모듈 가져옴
def intersect(*ar):
	"교집합"
	return reduce(__intersectSC, ar)

def __intersectSC(listX, listY):
	setList = []
	for x in listX:
		if x in listY:
			setList.append(x)
	return setList

def difference(*ar):
	"차집합"
	setList = []
	intersectSet = intersect(*ar)
	unionSet = union(*ar)
	for x in unionSet:
		if not x in intersectSet:
			setList.append(x)
	return setList

def union(*ar):
	"합집합"
	setList = []
	for item in ar:
		for x in item:
			if not x in setList:
				setList.append(x)
	return setList
#실행
>>> import simpleset
>>> dir(simpleset)
['WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', '__builtins__', '__cached__',
 '__doc__', '__file__', '__intersectSC', '__loader__', '__name__',
 '__package__', '__spec__', 'cmp_to_key', 'difference', 'intersect',
 'lru_cache', 'partial', 'partialmethod', 'reduce', 'singledispatch',
 'total_ordering', 'union', 'update_wrapper', 'wraps']
>>> setA = [1,3,5,7,10]
>>> setB = [2,3,4,9]
>>> simpleset.union(setA, setB)
[1, 3, 5, 7, 10, 2, 4, 9]
>>> simpleset.intersect(setA, setB, [1,2,3])
[3]
