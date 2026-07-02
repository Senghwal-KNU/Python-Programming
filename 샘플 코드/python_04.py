def q6_5_1(): 
    lst2 = ['pancake.', 'kiwi juice.', 'espresso.']
    
    for x in lst2: 
        print(f'I like {x}')
        
def q6_5(): 
    lst1 = ['I like', 'I love']
    lst2 = ['pancake.', 'kiwi juice.', 'espresso.']
    
    for x in lst1: 
        for y in lst2: 
            print(f'{x} {y}')

def q6_3(): 
    list1 = [3, 5, 7]
    list2 = [2, 3, 4, 5, 6]

    for x in list1: 
        for y in list2: 
            print(f'{x} X {y} = {x*y}')

def q6_8(): 
    lst = [10, 20, 30, 50, 60]

    m = 1

    for x in lst: 
        m *= x

    print('리스트의 원소들의 곱:', m)

def for_range_test1(): 
    for _ in range(5):   
        print('Hello, python!') 

    for x in range(5): 
        print(x) 

        
    print('1이상 100이하의 정수: ', end = '')
    for x in range(1, 101): 
        print(x, end = ' ')
    print()    

    print('1이상 100이하의 짝수: ', end = '')
    for x in range(2, 101, 2): 
        print(x, end = ' ')
    print()  

    print('1이상 100이하의 홀수: ', end = '')
    for x in range(1, 101, 2): 
        print(x, end = ' ')
    print()  

    print('100, 98, 96, …, 0: ', end = '')
    for x in range(100, -1, -2): 
        print(x, end = ' ')
    print()  

    print('-100 이상의 음수: ', end = '')
    for x in range(-100, 0): 
        print(x, end = ' ')
    print()  
    
    
def for_range_test2(): 
    s = 0
    for x in range(1, 11): 
        s += x    
    print('1 이상 10 이하의 정수의 합:', s)

    s = 0 #다시 초기화 
    for x in range(2, 101, 2): 
        s += x    
    print('1 이상 100 이하의 짝수의 합:', s)

    s = 0
    m = 1
    n = int(input('n: '))
    for x in range(1, n+1): 
        s += x    
        m *= x
    print(f'1 이상 {n} 이하 정수 합:', s)
    print(f'{n}!:', m)


def gugu_3_1(): 
    while True: 
        dan = int(input('단: '))
        if 2<=dan<=9:
            break
        else: 
            print('[입력오류] 2 이상 9 이하의 정수를 입력해주세요.')
            
    for x in range(1, 10): 
        print(f'{dan} X {x} = {dan*x:2d}') 


def gugu_3_2(): 
    for dan in range(2, 10): 
        for x in range(1, 10): 
            print(f'{dan} X {x} = {dan*x:2d}', end = ' '*3) 
        print() #개행


def gugu_3_3(): 
    for x in range(1, 10): 
        for dan in range(2, 10): 
            print(f'{dan} X {x} = {dan*x:2d}', end = ' '*3) 
        print() 
    


def gbb_test():   
    while True: 
        usr = input('가위, 바위, 보 중 하나를 선택하세요: ')
        #if usr in '가위, 바위, 보': #'위'도 통과해버리므로 안됨. 
        # if usr in ['가위', '바위', '보']: 
        if usr in '가위 바위 보'.split():
            break  
        else: 
            print('[입력오류] 가위, 바위, 보 중 하나를 선택하세요.')

    print(f'{usr}를 선택하셨습니다.')
    

def positive_test(): 
    while True:
        num = int(input('양의 정수: '))
        if num>0: 
            break
        else: 
            print('[입력오류] 양의 정수를 입력해주세요.')

    s = 0
    for x in range(1, num+1): 
        s += x
    print(f'1부터 {num}까지의 합:', s)


def quit_test(): 
    cnt = 0
    s = 0
    
    while True: 
        n = input('수: ') #아직 float()캐스팅 x -> quit 확인 후 캐스팅
        if n.upper().strip() == 'QUIT': 
            break
        else: 
            n = float(n)
            cnt += 1
            s += n    

    if cnt == 0: 
        print('입력된 수가 없습니다. ')
    else: 
        print(f'{cnt}개 수들의 평균: {s/cnt}')
        

def prime_test1(): 
    n = int(input('정수: '))
    cnt = 0
    
    for x in range(1, n+1): 
        if n%x == 0: 
            cnt += 1
            if cnt>2: 
                break

    if cnt == 2: 
        print(f'{n}는 소수입니다. ')
    else: 
        print(f'{n}는 소수가 아닙니다. ')
   

def prime_test2():
    a = int(input('a: '))    
    b = int(input('b: '))    

    prime_cnt = 0 #소수 발견시 증가
    
    if a>b: 
        a, b = b, a

    print(f'{a}와 {b} 사이의 소수: ', end ='')

    for n in range(a+1, b): 
        cnt = 0 #cnt: n 약수 개수
        #n이 바뀌면 0으로 재설정
        for x in range(1, n+1): 
            if n % x == 0: 
                cnt += 1
                if cnt>2:
                    break
        if cnt ==2: 
            print(n, end = ' ')
            prime_cnt+=1
    print()
    print(f'{a}와 {b} 사이의 소수 개수: {prime_cnt}')
             
    