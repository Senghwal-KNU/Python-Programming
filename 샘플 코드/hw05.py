import random 
import string

def lottery_test(): 
    target = random.sample(range(1, 11), 3)
    
    print('Debugging hint:', target)
    while True: 
        usr = [int(x) for x in input('복권번호 3개: ').split()]
        in_range_usr = [x for x in usr if 1<= x<=10]
        
        err_cnt = 0
        if len(usr)!= 3: 
            err_cnt += 1
            print('[입력오류] 번호 3개를 입력해주세요.') 
        if len(in_range_usr)!= len(usr): #3이 아니라 len(usr)랑 비교해야함.  
            err_cnt += 2
            print('[입력오류] 범위 내의 값을 입력해주세요.') 
        
        if err_cnt == 0: 
            break
    
    hit_cnt = 0
    for x in target: 
        if x in usr: 
            hit_cnt += 1
            
    if hit_cnt == 3: 
        print('1억원')
    elif hit_cnt == 2: 
        print('1천만원')
    elif hit_cnt == 1: 
        print('1만원')
    else: 
        print('다음 기회에...')
        
def pw_test():
    universe = string.ascii_letters+string.digits+'!@#$%~^&'
    
    while True: 
        pw = ''
        is_valid = [0]*4 #is_valid = [0,0,0,0]
        for _ in range(8): 
            pw += random.choice(universe)
            
        for x in pw: 
            if x.islower(): 
                is_valid[0] += 1
            elif x.isupper(): 
                is_valid[1] += 1
            elif x.isdigit(): 
                is_valid[2] += 1
            else: 
                is_valid[3] += 1
        
        if 0 not in is_valid: 
            break
            
    print('임시비밀번호:',pw)
        
def mul(a = 1, b = 1): 
    return a*b

def mul_test(): 
    print(mul(2,3))
    print(mul(2))
    print(mul())
        

def greet(): 
    print('환영합니다. ')
    
def q5_1(): 
    greet()
    greet()
    
    
def square(n): 
    return n*n
    
def q5_2(): 
    print('3의 제곱은 :', square(3))
    print('4의 제곱은 :', square(4))
    
def mile2km(m): 
    return m*1.61

def q5_4(): 
    for x in range(1, 6): 
        print(f'{x} 마일 =  {mile2km(x)} 킬로미터')
    
def inch2cm(inch): 
    return inch*2.54

def q5_5(): 
    for x in range(1, 6): 
        print(f'{x} 인치 =  {inch2cm(x)} 센티미터')        

def mean3(a, b, c): 
    return (a+b+c)/3
    
def max3(a, b, c): 
    rslt = a #일단은 a를 최댓값으로 두고, 더 큰 값 발견시 교체
    
    if rslt < b: 
        rslt = b
    if rslt < c: 
        rslt = c
        
    return rslt
    
def min3(a, b, c): 
    rslt = a 
    
    if rslt > b: 
        rslt = b
    if rslt > c: 
        rslt = c
        
    return rslt

def q5_7(): 
    a, b, c = [float(x) for x in input('세 수를 입력하시오: ').split()] # 5.4 9.1 -2.7
    
    print('평균:', mean3(a, b, c))
    print('최댓값:', max3(a, b, c))
    print('최솟값:', min3(a, b, c))

def sort(a, b, c): 
    if a>b: 
        a, b = b, a
    if a>c: 
        a, c = c, a
    #이 까지 수행하면, a에는 가장 작은 값 저장됨. 
    
    if  b>c: 
        b, c = c, b
        
    print(a, b, c, sep = ', ', end = '')
    

def q5_7_2(): 
    a, b, c = [float(x) for x in input('세 수를 입력하시오: ').split()] # 5.4 9.1 -2.7
    
    sort(a, b, c)
    print(f'의 평균값은 {mean3(a, b, c):.1f}')
    sort(a, b, c)
    print(f'의 최댓값은 {max3(a, b, c):.1f}')
    sort(a, b, c)
    print(f'의 최솟값은 {min3(a, b, c):.1f}')

def ft_call(): 
    # lottery_test()
    # pw_test()
    # mul_test()
    # q5_1()
    # q5_2()
    # q5_4()
    # q5_5()
    # q5_7()
    # q5_7_2()
    pass
    
ft_call()