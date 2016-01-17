#클래스

>>> class MyClass:
	"""아주 간단한 클래스"""
	pass

>>> dir()
['MyClass', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> type(MyClass) #MyClass타입 확인
<class 'type'>
>>> 
>>> 
>>> class Person:
	Name="Default Name"
	def print(self):
		print("My Name is {0}".format(self.Name))

		
>>> p1 = Person() #인스턴스 객체 생성
>>> p1.print() #멤버변수값을 출력
My Name is Default Name
>>> p1.Name="내 이름은 김연아!" #인스턴스 객체의 멤버 변수 값 변경
>>> p1.print() #바운드 메서드 호출
My Name is 내 이름은 김연아!
>>> Person.print(p1) #언바운드 메서드 호출 
My Name is 내 이름은 김연아!
=============================== RESTART: Shell ===============================
>>> class Person: #클래스 정의
	name = "Default Name"

	
>>> p1 = Person() #인스턴스 객체 생성
>>> p2 = Person()
>>> print("p1's name:", p1.name) #각 객체의 name속성 출력
p1's name: Default Name
>>> print("p2's name:",p2.name)
p2's name: Default Name
>>> p1.name="김연아" #p1.name 속성값 변경
>>> print("p1's name:", p1.name)
p1's name: 김연아

>>> Person.title = "New title" #클래스 객체에 새로운 멤버 변수 title추가
>>> print("p1's title: ", p1.title) #두 인스턴스 객체에 모두 접근 가능
p1's title:  New title
>>> print("p2's title: ", p2.title)
p2's title:  New title
>>> print("Person's title:", Person.title) #클래스 객체에서도 접근 가능
Person's title: New title
>>> dir(Person) #가장 뒤쪽에보면 name, title로 title이 클래스에 추가됨을 볼수있음
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'title']
>>> p1.age = 20 #p1객체에만 age 멤버변수 추가
>>> print("p1's title: ", p1.age)
p1's title:  20
>>> print("p2's title ", p2.age) #p2객체와 상위 Person 클래스에서 age 이름을 찾을수 없음
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print("p2's title ", p2.age) #p2객체와 상위 Person 클래스에서 age 이름을 찾을수 없음
AttributeError: 'Person' object has no attribute 'age'

=============================== RESTART: Shell ===============================
>>> #예제 5-3-1 멤버 메서드에서  self가 누락된 경우
>>> str = "NOT Class Member" #전역변수
>>> class GString:
	str = "" #클래스 객체 멤버 변수
	def Set(self, msg):
		self.str = msg
	def Print(self):
		print(str)
"""self를 이용해 클래스 멤버에 접근하지 않는 경우
이름이 동일한 전역변수에 접근해서 출력함"""
		
>>> g = GString()
>>> g.Set("Frist Message")
>>> g.Print()
NOT Class Member

"""주로 발생하는 실수 중 하나가 클래스 메서드 내에서 인스턴스(self)를
통하지 않고 변수에 접근하는것. 전역 변수와 클래스 변수의 이름이 동일한 경우
에러가 발생하지 않으므로 문제해결이 어렵다!!"""
#위의 예제에서 멤버메서드 Print()내부에서 인스턴스 객체 self를 통과하지 않고
#전역변수 str값을 출력하고 있다. 따라서 의도와는 다르게 전역변수 str값이 출력됨.
"""해결법: def Print(self): print(self.str)로 하면 정상 결과 출력"""

=============================== RESTART: Shell ===============================
>>> #__class__ 내장속성
>>> class Test:
	data = "Default"

	
>>> i2 = Test()
>>> i1 = Test()
>>> i1.__class__.data = "클래스 데이터 변경" #__class__속성을 이용해 클래스 데이터 변경
>>> #참조하는 모든 인스턴스가 변경됨
>>> print(i1.data)
클래스 데이터 변경
>>> print(i2.data)
클래스 데이터 변경
>>> i2.data="i2의 데이터만 변경" #i2 인스턴스 객체의 데이터만 변경
>>> print(i1.data)
클래스 데이터 변경
>>> print(i2.data)
i2의 데이터만 변경
>>> print(i2.__class__.data) #i2의 클래스 객체의 데이터는 변경되지 않음
클래스 데이터 변경

=============================== RESTART: Shell ===============================
>>> #예제 5-5-1 생성자, 소멸자
>>> class MyClass:
	def __init__(self, value): #생성자 메서드
		self.Value = value
		print("Class is created! Value = ", value)
	def __del__(self): #소멸자 메서드
		print("Class is deleted!")

		
>>> def foo():
	d = MyClass(10) #함수 foo 블록 안에서만 인스턴스 객체 d가 존재

	
>>> foo()
Class is created! Value =  10
Class is deleted!
=============================== RESTART: Shell ===============================
>>> #예제 5-6-1 CounterManager클래스
>>> class CounterManager:
	insCount = 0
	def __init__(self): #인스턴스 객체가 생성되면 클래스 영역의 insCount 변수 값 증가
		CounterManager.insCount += 1
	def printInstanceCount(): #인스턴스 객체 개수 출력
		print("Instance Count: ", CounterManager.insCount)

		
>>> a, b, c = CounterManager(), CounterManager(), CounterManager()
>>> CounterManager.printInstanceCount() #인스턴스 개수 출력
Instance Count:  3
>>> b.printInstanceCount() #암묵적으로 인스턴스 객체 받기 때문에 에러 발생
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    b.printInstanceCount()
TypeError: printInstanceCount() takes 0 positional arguments but 1 was given
=============================== RESTART: Shell ===============================
>>> #예제 5-6-2 정적메서드, 클래스 메서드를 적용한 CounterManager 클래스
>>> class CounterManager:
	insCount = 0
	def __init__(self):
		CounterManager.insCount += 1
	def staticPrintCount(): #정적 메서드 정의
		print("Instance Count: ", CounterManager.insCount)
	SPrintCount = staticmethod(staticPrintCount) #정적메서드로 등록
	
	def classPrintCount(cls): #클래스 메서드 정의(암무적으로 첫 인자는 클래스를 받음)
		print("Instance Count: ", cls.insCount)
	CPrintCount = classmethod(classPrintCount) #클래스 메서드로 등록

	
>>> a,b,c = CounterManager(), CounterManager(), CounterManager()
>>> CounterManager.SPrintCount() #정적 메서드로 인스턴스 객체 개수를 출력
Instance Count:  3
>>> b.SPrintCount()
Instance Count:  3
>>> CounterManager.CPrintCount() #클래스 메서드로 인스턴스 객체 개수를 출력
Instance Count:  3
>>> b.CPrintCount()
Instance Count:  3
=============================== RESTART: Shell ===============================
>>> #예제 5-7-1 수치 연산자 중복 정의 예제-1
>>> class GString:
	def __init__(self, init=None):
		self.content = init
	def __sub__(self, str): #'-'연산자 중복
		for i in str:
			self.content = self.content.replace(i, '')
		return GString(self.content)
	def __abs__(self): #abs() 내장함수 중복
		return GString(self.content.upper())
	def Print(self):
		print(self.content);

		
>>> g = GString("aBcdef")
>>> g -= "df" #'-'연산자가 중복된 경우 '-='도 지원
>>> g.Print()
aBce
>>> g = abs(g)
>>> g.Print()
ABCE
=============================== RESTART: Shell ===============================
>>> #예제 5-8-1 Person클래스
>>> class Person:
	"부모 클래스 "
	def __init__(self, name, phoneNumber):
		self.Name = name
		self.PhoneNumber = phoneNumber
	def PrintInfo(self):
		print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))
	def PrintPersonData(self):
		print("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

		
>>> class Student(Person):
	"자식 클래스"
	def __init__(self, name, phoneNumber, subject, studentID): #자식클래스 생성자 메서드
		self.Name = name
		self.PhoneNumber = phoneNumber
		self.Subject = subject
		self.StudentID = studentID

		
>>> p = Person("Derick", "010-123-4567")
>>> s = Student("Marry", "010-654-1234", "Computer Science", "990999")
>>> p.__dict__ #Person 인스턴스 객체
{'PhoneNumber': '010-123-4567', 'Name': 'Derick'}
>>> s.__dict__ #Student 인스턴스 객체
{'Subject': 'Computer Science', 'Name': 'Marry', 'StudentID': '990999',
 'PhoneNumber': '010-654-1234'}
=============================== RESTART: Shell ===============================
>>> #예제 5-8-2 부모 클래스의 생성자 호출 예제
>>> class Person:
	"부모 클래스 "
	def __init__(self, name, phoneNumber):
		self.Name = name
		self.PhoneNumber = phoneNumber
	def PrintInfo(self):
		print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))
	def PrintPersonData(self):
		print("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

		
>>> class Student(Person): #5-8-1의 예제에서 부모클래스랑 중복코드가 있어서 제거함
	def __init__(self, name, phoneNumber, subject, studentID):
		Person.__init__(self, name, phoneNumber) #명시적으로 Person 생성자 호출
		self.Subject = subject
		self.StudentID = studentID

		
>>> p=Person("Derick", "010-123-4567")
>>> s=Student("Marry", "010-654-1234", "Computer Science", "990999")
>>> p.__dict__
{'Name': 'Derick', 'PhoneNumber': '010-123-4567'}
>>> s.__dict__
{'PhoneNumber': '010-654-1234', 'Subject': 'Computer Science',
 'StudentID': '990999', 'Name': 'Marry'}
=============================== RESTART: Shell ===============================
>>> #예제5-8-3 자식 클래스에서 메서드를 추가하는 예제
>>> class Person:
	"부모 클래스 "
	def __init__(self, name, phoneNumber):
		self.Name = name
		self.PhoneNumber = phoneNumber
	def PrintInfo(self):
		print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))
	def PrintPersonData(self):
		print("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

>>> class Student(Person):
	"자식클래스"
	def __init__(self, name, phoneNumber, subject, studentID):
		Person.__init__(self, name, phoneNumber)
		self.Subject = subject
		self.StudentID = studentID
	def PrintStudentData(self): #새로운 메서드 추가
		print("Student(Subject: {0}, Student ID:{1})".format(self.Subject, self.StudentID))

		
>>> s = Student("Derick", "010-123-4567", "Computer", "990999")
>>> s.PrintPersonData() #Person으로부터 상속받은 메서드 호출
Person(Name:Derick, Phone Number: 010-123-4567)
>>> s.PrintStudentData() #Student에 추가된 메서드 호출
Student(Subject: Computer, Student ID:990999)
>>> dir(s) #상속받은 메서드와 추가된 메서드에 모두 접근 가능
['Name', 'PhoneNumber', 'PrintInfo', 'PrintPersonData', 'PrintStudentData',
 'StudentID', 'Subject', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__']
=============================== RESTART: Shell ===============================
>>> #예제 5-8-4 메서드 재정의
>>> class Person:
	"부모 클래스 "
	def __init__(self, name, phoneNumber):
		self.Name = name
		self.PhoneNumber = phoneNumber
	def PrintInfo(self):
		print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))
	def PrintPersonData(self):
		print("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

		
>>> class Student(Person):
	def __init__(self, name, phoneNumber, subject, studentID):
		Person.__init__(self, name, phoneNumber)
		self.Subject = subject
		self.StudentID = studentID
	def PrintStudentData(self):
		print("Student(Subject: {0}, Student ID: {1})".format(self.Subject, self.StudentID))
	def PrintInfo(self): #Person의 PrintInfo() 메서드 재정의
		print("Info(Name:{0}, Phone Number:{1})".format(self.Name, self.PhoneNumber))
		print("Info(Subject:{0}, Student ID:{1})".format(self.Subject, self.StudentID))

		
>>> s = Student("Derick", "010-123-4567", "Computer", "990999")
>>> s.PrintInfo() #재정의 된 메서드 호출
Info(Name:Derick, Phone Number:010-123-4567)
Info(Subject:Computer, Student ID:990999)
=============================== RESTART: Shell ===============================
>>> #예제 5-8-5 메서드 확장
>>> class Person:
	"부모 클래스 "
	def __init__(self, name, phoneNumber):
		self.Name = name
		self.PhoneNumber = phoneNumber
	def PrintInfo(self):
		print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))
	def PrintPersonData(self):
		print("Person(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

		
>>> class Student(Person):
	def __init__(self, name, phoneNumber, subject, studentID):
		Person.__init__(self, name, phoneNumber)
		self.Subject = subject
		self.StudentID = studentID
	def PrintStudentData(self):
		print("Student(Subject: {0}, Student ID: {1})".format(self.Subject, self.StudentID))
	def PrintInfo(self):
		Person.PrintPersonData(self) #명시적으로 Person 클래스의 PrintPersonData()를 호출
		print("Info(Subject:{0}, Student ID:{1})"
                      .format(self.Subject, self.StudentID))

=============================== RESTART: Shell ===============================
>>> #예제 5-8-8 Animal 클래스의 생성자가 두 번 호출되는 예제
>>> class Animal:
	def __init__(self):
		print("Animal __init__()")

		
>>> class Tiger(Animal):
	def __init__(self): 
		Animal.__init__(self) #Animal 생성자 메서드호출
		print("Tiger __intit()")

		
>>> class Lion(Animal):
	def __init__(self):
		Animal.__init__(self) #Animal 생성자 메서드호출
		print("Lion __init__()")

		
>>> class Liger(Tiger, Lion):
	def __init__(self):
		Tiger.__init__(self) #Tiger 생성자 메서드호출
		Lion.__init__(self) #Lion 생성자 메서드호출
		print("Liger __init__()")

		
>>> l = Liger()
Animal __init__() #Tiger 클래스에 의해 호출된것
Tiger __intit()
Animal __init__() #Lion 클래스에 의해 호출된것
Lion __init__()
Liger __init__()
=============================== RESTART: Shell ===============================
>>> #예제 5-8-9 Animal클래스의 생성자가 한 번 호출 되는 예제
>>> class Animal:
	def __init__(self):
		print("Animal __init__()")

		
>>> class Tiger(Animal):
	def __init__(self):
		super().__init__() #부모클래스의 생성자 메서드 호출
		print("Tiger __init__()")

		
>>> class Lion(Animal):
	def __init__(self):
		super().__init__() #부모클래스의 생성자 메서드 호출
		print("Lion __init__()")

		
>>> class Liger(Tiger, Lion):
	def __init__(self):
		super().__init__() #부모클래스의 생성자 메서드 호출
		print("Liger __init__()")

		
"""각 클래스에서는 부모의 생성자를 호출하기 위해
단일상속이나 다중상속을 고려하지 않고 단지 super().__init__()만 호출하면 됨.
그결과 Liger에서 한번만 메서드 호출이 이루어짐"""

>>> l = Liger()
Animal __init__()
Lion __init__()
Tiger __init__()
Liger __init__()
