# 캡슐화: 속성을 비공개(외부에서 접근 못하게)
# 속성명을 밑줄로 시작
# Dog 클래스
# - 속성: 이름, 나이, 몸무게

class Dog:
    def __init__(self,name='멍멍이',age=1,wt=1.5):
        self.__name=name
        self.__age=age
        self.__wt=wt

    def __str__(self):  # 객체를 문자열로 표현(배포용)
        return f'{self.__wt}kg, {self.__age}세, {self.__name}입니다.'
    
    def __repr__(self): # 객체를 대표하는 문자열 반환(디버깅용), __str__없으면 __str__역할도 함, repr(객체이름)으로 호출
        return f'{self.__wt}kg, {self.__age}세, {self.__name}입니다.'
    
    def rename(self,name):
        self.__name=name

    def get_age(self):
        return self.__age
    
    def __eq__(self,other):
        return self.__age==other.__age
    
    def __gt__(self,other):
        return self.__age>other.__age
    
    def __add__(self,other):
        import random
        newname=random.choice(self.__name)+random.choice(other.__name)
        return Dog(newname,0)
    
    def __sub__(self,other):
        
        return self.__wt-other.__wt
    
def test_dog():
    pp=Dog('뽀삐',4,2.4)
    wht=Dog('흰둥이',5,5.9)
    
    
 
    print(pp)
    print(wht)

    # print('흰둥이 나이:',wht.__age)
    # whtage=wht.__age
    # print(wht.__age)
    print(wht)
    
    my_dog=Dog()
    print(my_dog)

    lst=[pp,wht,my_dog]
    for x in lst:
        print(x)
    print(lst)
    print(pp==wht)
    print(max(lst))
    baby_dog=pp+wht
    lst.append(baby_dog)
    baby_dog.rename('포실이')
    print(lst)
    print(f'{pp-wht:.2f}')  # 몸무게 차이 반환
# test_dog()

def p_4():
    class Vector:
        def __init__(self,x=0,y=0):
            self.x=x
            self.y=y
            
        def __str__(self):
            return f'{(self.x,self.y)}'
            
        def __mul__(self,other):
            return Vector(self.x*other.x,self.y*other.y)
            
        def __truediv__(self,other):
            return Vector(self.x/other.x,self.y/other.y)
            
        def __neg__(self):
            return Vector(-1*self.x,-1*self.y)
            
        def v_mag(v):
            return (v.x**2+v.y**2)**0.5
            
        def __gt__(self,other):
            return self.v_mag()>other.v_mag()
            
        def __le__(self,other):
            return not self.v_mag()>other.v_mag()
            
        def __ge__(self,other):
            return self.v_mag()>=other.v_mag()
            
        def __lt__(self,other):
            return not self.v_mag()>=other.v_mag()
            
    v = Vector()
    print(v)
    
    print()
    
    v1 = Vector(30, 40)
    v2 = Vector(10, 20)
    print(v1*v2)
    print(v1/v2)
    print(-v1)
    
    print()
    
    print(v1>v2) #벡터의 크기 비교
    print(v1>=v2)
    print(v1<v2)
    print(v1<=v2)
# p_4()

def id_test():
    lst=[1,2,3,4]
    cpy=lst # cpy에 [1,2,3,4](객체)가 저장되는 게 아니라 lst의 주소값 저장
    cpy.remove(2)
    print(cpy,id(cpy))
    print(lst,id(lst)) # 원본도 바뀜
    lst.remove(3)
    print(cpy,id(cpy)) # 복사본도 바뀜
    print(lst,id(lst)) 
    
    real_cpy=lst[:]
    print(real_cpy,id(real_cpy))
    
    
id_test()