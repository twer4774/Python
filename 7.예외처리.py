#예외처리

>>> #예제 7-3-3 else와 finally
>>> def divide(a, b):
	return a/b

>>> try:
	c = divide(5,2)
except ZeroDivisionError:
	print('두 번째 인자는 0이어서는 안됩니다.')
except TypeError:
	print('모든 인자는 숫자여야합니다.')
except:
	print('ZeroDivisionError, TypeError를 제외한 다른 에러')
else: #예외가 발생하지 않는 경우
	print('Result: {0}'.format(c))
finally: #예외 발생 여부와 상관없이 수행
	print('항상 finally 블록은 수행됩니다.')

	
Result: 2.5
항상 finally 블록은 수행됩니다.
=============================== RESTART: Shell ===============================
>>> #예제 7-3-4 예외에 대한 정보를 전달받는 예제
>>> def divide(a,b):
	return a/b

>>> try:
	c = divide(5, "af")
except TypeError as e: #전달되는 예외 인스턴스 객체를 e로 받아서 사용
	print('에러: ', e.args[0])
except Exception:
	print('음~ 무슨 에러인지 모르겠어요!!')

	
에러:  unsupported operand type(s) for /: 'int' and 'str'

=============================== RESTART: Shell ===============================
>>> #예제 7-3-5 에러를 묶어서 처리하는 예제
>>> def divide(a,b):
	return a/b

>>> try:
	c = divide(5,0)
except (ZeroDivisionError, OverflowError, FloatingPointError):
	print('수치 연산 관련 에러입니다.') #명시된 에러 모두 처리
except TypeError:
	print('모든 인자는 숫자여야 합니다.')
except Exception:
	print('무슨 에러인지 모르겠어요')

	
수치 연산 관련 에러입니다.
=============================== RESTART: Shell ===============================
>>> #예제 7-3-6 상위 에러를 처리해 하위의 모든 에러를 처리하는 예제
>>> def divide(a, b):
	return a/b

>>> try:
	c = divide(5,0)
except ArithmeticError: #상위 클래스를 처리할 때 하위의 모든 클래스도 이부분에서 처리
	print('수치 연산 관련 에러입니다.')
except TypeError:
	print('모든 인자는 숫자여야합니다.')
except Exception:
	print('무슨 에러인지 모르겠어요')

	
수치 연산 관련 에러입니다.
=============================== RESTART: Shell ===============================
>>> #예제 7-4-1 내장 예외 발생
>>> def RaiseErrorFunc():
	raise NameError #내장 예외인 NameError발생

>>> try:
	RaiseErrorFunc()
except:
	print("NameError is Catched")

	
NameError is Catched
=============================== RESTART: Shell ===============================
>>> #예제 7-4-2 내장 예외 전달
>>> def RaiseErrorFunc():
	raise NameError("NameError의 인자")

>>> def PropagateError():
	try:
		RaiseErrorFunc()
	except:
		print("에러 전달 이전에 먼저 이 메시지가 출력됩니다.")
		raise #발생한 에러를 상위로 전달

>>> PropagateError()
에러 전달 이전에 먼저 이 메시지가 출력됩니다.
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    PropagateError()
  File "<pyshell#119>", line 3, in PropagateError
    RaiseErrorFunc()
  File "<pyshell#112>", line 2, in RaiseErrorFunc
    raise NameError("NameError의 인자")
NameError: NameError의 인자
=============================== RESTART: Shell ===============================
>>> #예제 7-5-1 사용자정의 예외
>>> class NegativeDivisionError(Exception): #사용자정의 예외 정의
	def __init__(self,value):
		self.value=value

		
>>> def PositiveDivide(a,b):
	if(b<0): #제수가 0보다 작은 경우, NegativeDivisionErro발생
		raise NegativeDivisionError(b)
	return a/b

>>> try:
	ret = PositiveDivide(10,-3)
	pirnt('10/-3 = {0}'.format(ret))
except NegativeDivisionError as e: #사용자정의 예외인 경우
	print('Error - Second argument of PositiveDivide is', e.value)
except ZeroDivisionError as e: #0으로 나누는 경우
	print('Error -', e.args[0])
except: #그 외 모든 예외의 경우
	print("Unexpected exception!")

	
Error - Second argument of PositiveDivide is -3
