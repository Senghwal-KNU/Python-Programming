class Counter: 
    def __init__(self, number = 0): 
        if number in range(100): 
            self._number = number
        else: 
            self._number = 0
    
    def reset(self): 
        self._number = 0
        
    def inc(self): 
        self._number += 1
        if self._number >= 100: 
            self._number = 0
        
    def dec(self): 
        self._number -= 1
        if self._number <0: 
            self._number = 0
            
    def __str__(self): 
        return f'C({self._number})'
        
    def __add__(self, other): 
        return Counter(self._number + other._number)
        
    def __sub__(self, other): 
        return Counter(self._number - other._number)

def cnt_test1(): 
    c1 = Counter(10)
    c1.inc()
    print('c1 =', c1)
    c2 = Counter(99)
    c2.inc()
    print('c2 =', c2)
        
def cnt_test2(): 
    c1 = Counter()
    c1.inc()
    c1.inc()
    print('c1 =', c1)
    c1.reset()
    print('c1 =', c1)
    c1.dec()
    print('c1 =', c1)
    
def cnt_test3(): 
    c1 = Counter(90)
    c2 = Counter(20)
    print('c1 + c2 =', c1 + c2)
    print('c1 - c2 =', c1 - c2)
    
# cnt_test1()   
# cnt_test2()   
# cnt_test3()  

class BankAccount: 
    def __init__(self, name, acc_num, balance = 0):    
        self._name = name
        self._acc_num = acc_num
        self._balance = balance
    
    def __str__(self): 
        return f'{self._name}님의 계좌 {self._acc_num}의 잔고는 {self._balance:,}원입니다.'
        
    def deposit(self, money): 
        if money>=0:
            self._balance += money
            print(f'{money:,}원이 입금되었습니다. 잔고는 {self._balance:,}원입니다.')
        else: 
            print('출금 기능을 사용해주세요. ')
            
    def withdraw(self, money): 
        if money in range(self._balance+1):
            self._balance -= money
            print(f'{money:,}원이 인출되었습니다. 잔고는 {self._balance:,}원입니다.')
        elif money > self._balance: 
            print(f'[Error] 잔고 내에서만 출금 가능합니다. 잔고: {self._balance:,}, 출금 요청 금액: {money:,}')
        else: 
            print('입금 기능을 사용해주세요. ')
    
    def __eq__(self, other): 
        return self._name == other._name
    
    def __ne__(self, other): 
        return self._name != other._name
    
    def __lt__(self, other): 
        return self._balance < other._balance
    def __gt__(self, other): 
        return self._balance > other._balance
    def __le__(self, other): 
        return self._balance <= other._balance
    def __ge__(self, other): 
        return self._balance >= other._balance
    
            
def ba_test1(): 
    account1 = BankAccount("홍길동", "1234-0001")
    print(account1)
    account1.deposit(2000) #2000원을 입금
    print(account1)
    account1.withdraw(500) # 500원을 출금
    print(account1)
    account1.withdraw(5000) #5000원을 출금
    
def ba_test2(): 
    account1 = BankAccount("홍길동", "1234-0001")
    account2 = BankAccount("홍길동", "1234-0002", 2000)
    account3 = BankAccount("둘리", "1234-0003", 50000)
    print(account1==account2)
    print(account1!=account2)
    print(account1<account3)
    print(account2<=account3)
    print(account2>account3)
    
# ba_test1()   
# ba_test2()  
  
class Car: 
    def __init__(self, color = 'silver', mileage = 0):
        self.__color = color
        self.__mileage = mileage
        
    def go_straight(self, dist): 
        print(f'{dist}m 직진합니다. ')
        self.__mileage+=dist
    
    def turn_right(self): 
        print('우회전 후 ', end = '')
        
    def turn_left(self): 
        print('좌회전 후 ', end = '')
        
    def __str__(self): 
        return f'[Car] color: {self.__color}, mileage: {self.__mileage}'
    
    def get_mileage(self): 
        return self.__mileage
    
def car_test(): 
    c = Car('red')
    print(c)
    c.go_straight(25)
    c.turn_left()
    c.go_straight(30)
    c.turn_right()
    c.go_straight(15)
    c.turn_left()
    c.go_straight(20)
    print(f'총 주행 거리는 {c.get_mileage()}m 입니다. ')
    
# car_test()

class Elevator: 
    def __init__(self, floor = 0, is_open = False):
        if floor in range(-2, 11): 
            self._floor = floor
        else: 
            self._floor = 0
        
        self._is_open = bool(is_open)
        
    def move(self, destination) : 
        self.close()
        if destination not in range(-2, 11): 
            print('유효한 층수를 입력해주세요.')
        else: 
            #도착 층 안내
            print(f'{self.to_str_floor(destination)}층으로 이동합니다.')            
            #이동 층수 설정
            if self._floor<=destination : 
                move_range = range(self._floor, destination+1)
            else: 
                move_range = range(self._floor, destination-1, -1)
            
            #이동 과정 출력
            for x in move_range:  
                self._floor = x
                print(self.to_str_floor(), end = ' ')
            print()
            
            #도착하면 문 열기 
            self.open()
            
    
    def to_str_floor(self, floor = None): 
        if floor == None: 
            floor = self._floor
            
        if floor == 0: 
            rslt = 'L'
        elif floor < 0: 
            rslt = f'B{-floor}'
        else: 
            rslt = str(floor)
        return rslt
        
        
    def close(self): 
        if self._is_open == True: 
            self._is_open = False
            print('문이 닫힙니다.')
            
    def open(self): 
        if self._is_open == False: 
            self._is_open = True
            print('문이 열립니다.')
            
            
    def __str__(self): 
        if self._is_open == True: 
            door_state = '열려'
        else: 
            door_state = '닫혀'
            
        return f'이 엘레베이터는 현재 {self.to_str_floor()}층에 있으며, 문이 {door_state}있습니다.'
        
            
            

def el_test1(): 
    e = Elevator() # 엘레베이터 생성
    print(e)
    e.open() # 엘레베이터의 문을 연다
    e.close() # 엘레베이터의 문을 연다
    
    
    
def el_test2(): 
    e = Elevator()
    print(e)
    e.move(2) # 2층으로 이동
    print(e)
    print()
    e.move(-2) # 지하 2층으로 이동
    print(e)
    
def el_test3(): 
    e = Elevator(5, True)
    print(e)
    print()
    e.move(-10)
    print(e)
    
    

# el_test1()
# el_test2()
# el_test3()


class Train: 
    def __init__(self, car_cnt = 1, capacity = 50): 
        if car_cnt<=0: 
            car_cnt = 1
        self._car_cnt = car_cnt
        
        if capacity <= 0: 
            capacity = 50
        self._capacity = capacity
        
    def __str__(self): 
        return '이 열차는 총 {}칸으로 구성되며, 수용인원은 {}명입니다.'.format(self._car_cnt, self._capacity)
        
    def append(self, car_cnt, capacity): 
        err_cnt = 0
        if car_cnt<=0: 
            print('[오류] 양수 개의 칸만 연결할 수 있습니다. ')
            err_cnt += 1
        if capacity <= 0: 
            print('[오류] 추가 수용 인원은 양수만 가능합니다. ')
            err_cnt += 2
        
        if err_cnt == 0: 
            self._car_cnt += car_cnt
            self._capacity += capacity
        
    def __le__(self, other): 
        return self._capacity <= other._capacity
        
    def __lt__(self, other): 
        return self._capacity < other._capacity
        
    def __ge__(self, other): 
        return self._capacity >= other._capacity
        
    def __gt__(self, other): 
        return self._capacity > other._capacity
        
    def __add__(self, other): 
        return Train(self._car_cnt+other._car_cnt, self._capacity+other._capacity)
        
def train_test(): 
    semaeul1 = Train() # 1칸으로 구성된 수용인원 50명의 열차 생성 후 새마을1호에 저장
    print('새마을 1호:',  semaeul1)
    semaeul1.append(3,  200) # 새마을1호에 3칸 추가(수용 인원 200명 추가)
    print('새마을 1호:', semaeul1)

    semaeul2 = Train(5, 200)# 5칸으로 구성된 수용인원 200명의 열차 생성 후 새마을2호에 저장
    print('새마을 2호:', semaeul2)

    print('새마을 1호 수용인원 > 새마을 2호 수용인원:', semaeul1 > semaeul2)
    print('새마을 1호 + 새마을 2호 :', semaeul1 + semaeul2)
    print('새마을 1호:', semaeul1)
    
# train_test()

class Vector: 
    def __init__(self, x = 0, y = 0): 
        self.x = x
        self.y = y
        
    def __str__(self): 
        return  f'({self.x}, {self.y})'
        
    def __mul__(self, other): 
        return Vector(self.x * other.x , self.y * other.y)
        
    def __truediv__(self, other): 
        return Vector(self.x / other.x , self.y / other.y)
        
    def __neg__(self): 
        return Vector(-self.x, -self.y)
        
    def __gt__(self, other): 
        return self.x**2+self.y**2 > other.x**2+other.y**2
        
    def __ge__(self, other): 
        return self.x**2+self.y**2 >= other.x**2+other.y**2
        
    def __lt__(self, other): 
        return self.x**2+self.y**2 < other.x**2+other.y**2
        
    def __le__(self, other): 
        return self.x**2+self.y**2 <= other.x**2+other.y**2
        
        
def vector_test1(): 
    v = Vector() 
    print(v)
    
def vector_test2(): 
    v1 = Vector(30, 40)
    v2 = Vector(10, 20)
    print(v1*v2) 
    print(v1/v2)
    print(-v1)
    
def vector_test3(): 
    v1 = Vector(30, 40)
    v2 = Vector(10, 20)
    print(v1>v2) 
    print(v1>=v2)
    print(v1<v2) 
    print(v1<=v2)
    
# vector_test1()
# vector_test2()
# vector_test3()

