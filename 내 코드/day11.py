# hasattr(object,name) name의 매개변수로 object를 넣을 수 있는지 반환

def class_test():
    # 강아지에게 {이름}야, 안녕, 배고프면 밥주고 아니면 놀아주는 기능
    class Dog:
        #속성: 나이, 이름, 몸무게, 키, ... => 필요한 속성만 추리자 (추상화) => 이름, 포만감 필요
        def speak(self):
            print('bowbow')
        def hello(self):
            print('hi')
    
    moco=Dog()
    moco.speak()
    moco.hello()
# class_test()

# 스페셜 메소드: __메소드이름__ 형태의 메소드
# 1. 자동으로(implicit) 호출됨
def class_test2():
    class Dog:
        def __init__(self,name,fulness):
            self.name=name
            self.fulness=fulness
        def speak(self):
            print('멍멍')
        def hello(self):
            print('멍하')
        def eat(self,food):
            print(f'{self.name}아 {food}먹어라~')
            self.fulness+=3
        def play(self,toy='공'):
            print(f'{toy}놀이를 하는 {self.name}')
            self.fulness-=1
            
    test_dog=Dog('댕댕',7)        
            
    if test_dog.fulness<=5:
        test_dog.eat('밥')
    else:
        test_dog.play()
# class_test2()
            

def class_9_8():
    class Counter:
        def __init__(self,number=0):
            if number>=100 or number<0:
                self._number=0
            else:
                self._number=number
        
        def reset(self):
            self._number=0
            
        def inc(self):
            self._number+=1
            if self._number>=100:
                self.reset()
            
        def dec(self):
            self._number-=1
            if self._number<0:
                self.reset()
                
        def __str__(self):
            return f'C({self._number})'
            
        def __add__(self,other):
            return Counter(self._number+other._number)
        
        def __sub__(self,other):
            return Counter(self._number-other._number)
        
    c1 = Counter(10)
    c1.inc()
    print('c1 =', c1)
    c2 = Counter(99)
    c2.inc()
    print('c2 =', c2)
    
    print()
    
    c1 = Counter()
    c1.inc()
    c1.inc()
    print('c1 =', c1)
    c1.reset()
    print('c1 =', c1)
    c1.dec()
    print('c1 =', c1)
    
    print()
    
    c1 = Counter(90)
    c2 = Counter(20)
    print('c1 + c2 =', c1 + c2)
    print('c1 - c2 =', c1 - c2)
# class_9_8()

def class_9_10():
    class BankAccount:
        def __init__(self, name, account_num, balance=0):
            self.name=name
            self.account_num=account_num
            self.balance=balance
            
        # 입금 기능
        def deposit(self,money):
            if money<0:
                print(f'[Error] 출금 기능을 사용하세요.')
            else:
                self.balance+=money
                print(f'{money}원이 입금되었습니다. 잔고는 {self.balance:,}원입니다.')
                    
        # 출금 기능
        def withdraw(self,money):
            if money<0:
                print(f'[Error] 입금 기능을 사용하세요.')
            else:
                if self.balance<money:
                    print(f'[Error] 잔고 내에서만 출금 가능합니다. 잔고: {self.balance:,}, 출금 요청 금액: {money}')
                else:
                    self.balance-=money
                    print(f'{money}원이 인출되었습니다. 잔고는 {self.balance:,}원입니다.')
            
        def __str__(self):
            return f'{self.name}님의 계좌 {self.account_num}의 잔고는 {self.balance:,}원입니다.'
        
        def __lt__(self,other):
            return self.balance<other.balance
        
        def __le__(self,other):
            return self.balance<=other.balance
        
        def __gt__(self,other):
            return self.balance>other.balance
        
        def __ge__(self,other):
            return self.balance>=other.balance
            
        def __eq__(self,other):
            return self.name==other.name or self.balance==other.balance
        
    account1 = BankAccount("홍길동", "1234-0001")
    print(account1)
    account1.deposit(2000) #2000원을 입금
    print(account1)
    account1.withdraw(500) # 500원을 출금
    print(account1)
    account1.withdraw(5000) #5000원을 출금
    
    print()
    
    account1 = BankAccount("홍길동", "1234-0001")
    account2 = BankAccount("홍길동", "1234-0002", 2000)
    account3 = BankAccount("둘리", "1234-0003", 50000)
    print(account1==account2)
    print(account1!=account2)
    print(account1<account3)
    print(account2<=account3)
    print(account2>account3)
# class_9_10()

def p_1():
    class Car:
        def __init__(self,color='silver',mileage=0):
            self.color=color
            self.mileage=mileage
        
        def __str__(self):
            return f'[Car] color: {self.color}, mileage: {self.mileage}'
        
        def go_ahead(self,m):
            print(f'{m}m 직진합니다.')
            self.mileage+=m
        
        def turn_left(self):
            print('좌회전 후 ',end='')
        
        def turn_right(self):
            print('우회전 후 ',end='')            
        
    my_car = Car('red')
    print(my_car)
    my_car.go_ahead(25)
    my_car.turn_left()
    my_car.go_ahead(30)
    my_car.turn_right()
    my_car.go_ahead(15)
    my_car.turn_left()
    my_car.go_ahead(20)
    print(f'총 주행 거리는 {my_car.mileage}m 입니다.')
# p_1()
    
    
# 속성을 비공개(private)로 한다 = 캡슐화
# -> 외부에서 속성을 변경할 수 없음
def p_2():
    class Elevator:
        def gen_floor(self,n):
            if n==0:
                floor='L'
            elif n<0:
                floor=f'B{n*-1}'
            else:
                floor=n
            return floor
            
        def gen_is_open(self,tf):
            if tf:
                return '열려'
            else:
                return '닫혀'
        
        def __init__(self,floor=0,is_open=False):
            if floor in range(-2,10+1):
                self._floor=floor
            else:
                self._floor=0
            self._is_open=bool(is_open)
            
        def __str__(self):
            return f'이 엘레베이터는 현재 {self.gen_floor(self._floor)}층에 있으며, 문이 {self.gen_is_open(self._is_open)}있습니다.'
            

            
        def close(self):
            if self._is_open:
                print("문이 닫힙니다.")
                self._is_open=False
                

        def open(self):
            if not self._is_open:
                print('문이 열립니다.')
                self._is_open=True
        
        def move(self,destination):
            self.close()
            if destination in range(-2,10+1):
                print(f'{self.gen_floor(destination)}층으로 이동합니다.')

                if self._floor==destination:
                    print(f'이미 {self.gen_floor(self._floor)}층입니다.')
                else:
                    if self._floor>destination: # go down
                        for i in range(self._floor,destination-1,-1):
                            print(self.gen_floor(i),end=" ")
                            self._floor=i
                        print()
                    else: # go up
                        for i in range(self._floor,destination+1, 1):
                            print(self.gen_floor(i),end=" ")
                            self._floor=i
                        print()
                self.open()
            else:
                print('유효한 층수를 입력해주세요.')
    

    e = Elevator() # 엘레베이터 생성
    print(e)
    e.open() # 엘레베이터의 문을 연다
    e.close() # 엘레베이터의 문을 연다  

    print()
    
    e = Elevator()
    e.move(2) # 2층으로 이동
    e.move(-2) # 지하 2층으로 이동
    print(e)
    
    print()
    
    e = Elevator(5, True)
    e.move(-10) #유효하지 않은 층수인 지하 10층으로 이동
    print(e)
# p_2()

def p_3():
    class Train:
        def __init__(self,car_cnt=1,capacity=50):
            if car_cnt<1:
                self.car_cnt=1
            else:
                self.car_cnt=car_cnt
            if capacity<0:
                self.capacity=50
            else:
                self.capacity=capacity
        
        def append(self,car_cnt,capacity):
            if car_cnt>0 and capacity>0:
                self.car_cnt+=car_cnt
                self.capacity+=capacity
            else:
                print('error')
        
        def __str__(self):
            return f'이 열차는 총 {self.car_cnt}칸으로 구성되며, 수용인원은 {self.capacity}명입니다.'
        
        def __gt__(self,other):
            return self.capacity>other.capacity
            
        def __add__(self,other):
            return f'이 열차는 총 {self.car_cnt+other.car_cnt}칸으로 구성되며, 수용인원은 {self.capacity+other.capacity}명입니다.'
        
    semaeul1 = Train() # 1칸으로 구성된 수용인원 50명의 열차 생성 후 새마을1호에 저장
    print('새마을 1호:',  semaeul1)
    semaeul1.append(3,  200) # 새마을1호에 3칸 추가(수용 인원 200명 추가)
    print('새마을 1호:', semaeul1)

    semaeul2 = Train(5, 200)# 5칸으로 구성된 수용인원 200명의 열차 생성 후 새마을2호에 저장
    print('새마을 2호:', semaeul2)

    print('새마을 1호 수용인원 > 새마을 2호 수용인원:', semaeul1 > semaeul2)
    print('새마을 1호 + 새마을 2호 :', semaeul1 + semaeul2)
    print('새마을 1호:', semaeul1)
# p_3()

def p_4():
    
    def gs(v):
        return (v.x**2+v.y**2)**0.5
    
    class Vector:
        def __init__(self,x=0,y=0):
            self.x=x
            self.y=y
        
        def __str__(self):
            return f'{(self.x,self.y)}'
            
        def __mul__(self,other):
            return (self.x*other.x,self.y*other.y)
        
        def __truediv__(self,other):
            return (self.x/other.x,self.y/other.y)
            
        def __neg__(self):
            return (-1*self.x,-1*self.y)
            
        def __gt__(self,other):
            return gs(self)>gs(other)
            
        def __ge__(self,other):
            return gs(self)>=gs(other)
            
        def __le__(self,other):
            return not gs(self)>gs(other)
            
        def __lt__(self,other):
            return not gs(self)>=gs(other)
        
    v = Vector()
    print(v)
    
    v1 = Vector(30, 40)
    v2 = Vector(10, 20)
    print(v1*v2)
    print(v1/v2)
    print(-v1)
    
    v1 = Vector(30, 40)
    v2 = Vector(10, 20)
    print(v1>v2) #벡터의 크기 비교
    print(v1>=v2)
    print(v1<v2)
    print(v1<=v2)
p_4()