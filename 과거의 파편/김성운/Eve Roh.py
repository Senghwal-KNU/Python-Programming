'''
중력절 17주년
class Counter:
    def __init__(self, value=0):
        self.count=value
    def increment(self):
        self.count+=1

a = Counter(100); a.increment()
print('a 카운터의 값=',a.count)
b = Counter(); b.increment()
print('b 카운터의 값=',b.count)
import math
class Circle:
    def __init__(self,radius=0):
        self.radius=radius
    def getArea(self):
        return math.pi*self.radius*self.radius
    def getPerimeter(self):
        return 2*math.pi*self.radius
c=Circle(10)
print('원의 면적:',c.getArea())
print('원의 둘레:',c.getPerimeter())
class Student:
    def __init__(self,name=None,age=0):
        self.__name=name
        self.__age=age
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age=age
    def setName(self,name):
        self.__name=name

obj=Student('홍길동', 20)
print(obj.getName())
print(obj.getAge())
class BankAccount:
    def __init__(self):
        self.__balance=0
    def withdraw(self,amount):
        self.__balance-=amount
        print('통장에', amount, '가 출금되었음')
    def deposit(self,amount):
        self.__balance+=amount
        print('통장에서', amount, '가 입금되었음')
    def show(self):
        print('잔액은', self.__balance)
a=BankAccount()
a.deposit(100)
a.withdraw(10)
class Television:
    serialnumber=0
    def __init__(self, channel, volume, on):
        self.channel=channel
        self.volume=volume
        self.on=on
        Television.serialnumber +=1
        self.number=Television.serialnumber
    def show(self):
        print(self.channel, self.volume, self.on, self.number)
myTV1=Television(11,10,True)
myTV1.show()
myTV2=Television(13,10,True)
myTV2.show()
myTV3=Television(5,23,True)
myTV3.show()
print(Television.serialnumber)
class student:
    tot=0;cnt=0
    def __init__(self, num, name, s):
        self.__num=num
        self.__name=name
        self.__score=s
        student.tot+=self.__score
        student.cnt+=1
    def show(self):
        print(self.__num, self.__name, self.__score)
    @staticmethod
    def avg():
        print('반 평균', student.tot/student.cnt)

s1=student(523, '노짱', 69); s2=student(818, '슨상', 74)
s1.show(); s2.show()
s1.avg()'''
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return Vector2D(self.x-other.x, self.y-other.y)
    def __eq__(self, other):
        return Vector2D(self.x==other.x, self.y==other.y)
    def __str__(self):
        return '(%g,%g)'%(self.x, self.y)
u=Vector2D(0,1)
v=Vector2D(1,0)
w=Vector2D(1,1)
a=u+v
print(u,'+',v,'=',a)
