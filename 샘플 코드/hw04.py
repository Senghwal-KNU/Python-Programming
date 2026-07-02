def print_10evens_ver1(): #방법 1
    while True: 
        n = int(input('양의 짝수: '))
        if n%2==0 and n>0: 
            break
        else: 
            print('[입력오류] 양의 짝수를 입력해주세요. ')
    
    for _ in range(10): #10번 반복
        print(n, end = ' ') #n 출력 후 
        n+=2        #2 증가 
    print()
    
def print_10evens_ver2(): #방법 2
    while True: 
        n = int(input('양의 짝수: '))
        if n%2==0 and n>0: 
            break
        else: 
            print('[입력오류] 양의 짝수를 입력해주세요. ')
    
    #n 이상의 연속된 짝수 10개를 range()로 생성
    for x in range(n, n+20, 2): 
        print(x, end = ' ')
    print()
    
 
def sum_atob(): 
    a = int(input('a: '))
    b = int(input('b: '))
    
    if a>b: 
        a, b = b, a#swap
        
    s = 0
    for x in range(a, b+1): 
        s += x
        
    print(f'{a} 이상 {b} 이하 수들의 합: {s}')
    
def pow_2(): 
    for n in range(1, 11):
        print(2**n, end = ' ')
    print()

def print_tops_ver1(): 
    tops = ['Shirts', 'Blouses', 'Sweaters', 'T-shirts', 'Hoodies']
    colors = ['Red', 'Blue', 'Yellow']
    
    for x in colors: 
        for y in tops: 
            print(f'{x:7s} {y}')
    
def print_tops_ver2(): 
    tops = ['Shirts', 'Blouses', 'Sweaters', 'T-shirts', 'Hoodies']
    colors = ['Red', 'Blue', 'Yellow']
    
    for x in tops: 
        for y in colors: 
            print(f'{y:7s} {x}')
    
    
def mul_nums(): 
    nums = [int(x) for x in input('정수: ').split()]

    exc5 = [x for x in nums if x%5!=0]
    m = 1
    for x in exc5: 
        m *= x
    print(f'5의 배수가 아닌 수들의 곱: {m}')
    
    
def avrg_until_neg1(): 
    s = 0
    cnt = 0
    while True: 
        usr = float(input('수: '))
        if usr == -1: 
            break
        else: 
            s += usr
            cnt += 1
    if cnt!=0: 
        print(f'{cnt}개 수들의 평균: {s/cnt}')
    else: 
        print('평균을 계산할 수가 없습니다. ')
    
def cnt_divisors(): 
    while True: 
        n = int(input('정수: '))
        if n>0: 
            break
        else: 
            print('[입력오류] 양의 정수를 입력해주세요. ')
            
            
    cnt = 0 #약수 개수
    #n%x==0 인 x의 개수를 카운팅
    #이때 x는 1이상 n이하의 정수
    
    for x in range(1, n+1): 
        if n%x == 0: 
            cnt += 1
            
    print(f'{n}의 약수 개수: {cnt}')
    
def print_divisors(): 
    while True: 
        n = int(input('정수: '))
        if n>0: 
            break
        else: 
            print('[입력오류] 양의 정수를 입력해주세요. ')
            
    
    for x in range(1, n+1): 
        if n%x == 0: 
            print(x, end = ' ')
            
def pow_sum(): 
    while True: 
        n = int(input('정수: '))
        if n>0: 
            break
        else: 
            print('[입력오류] 양의 정수를 입력해주세요. ')
            
    rslt = 0
    for x in range(1, n+1): 
        rslt += x**2
    
    print('결과:', rslt)
  
  