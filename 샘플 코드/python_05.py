import random 
import string 
import math

def gen_otp(): 
    for _ in range(6): 
        print(random.randint(0, 9), end ='')
    print()
    
    otp = ''

    for _ in range(6): 
        otp += str(random.randrange(10))
    print(otp)


def lottery_test(): 
    target = random.sample(range(1, 46), 6)
    print('이번 주 당첨 번호:', target)
    

def gen_pw(): 
    univ = string.ascii_letters+string.digits+string.punctuation
    #비복원추출
    pw = random.sample(univ, 8)
    for x in pw: 
        print(x, end = '')
    print()

    #복원추출 
    for _ in range(8): 
        x = random.choice(univ)
        print(x, end = '')  
    print() 


def nbr_game(): 
    target = random.randint(1, 20)
    cnt = 0 #시도횟수
    
    while True:  
        usr = int(input('1~20까지의 숫자를 입력하세요: '))
        cnt += 1

        if usr == target: 
            print('정답입니다!')
            break
        elif usr<target: 
            print(f'정답은 {usr} 보다 큽니다!')
        else: 
            print(f'정답은 {usr} 보다 작습니다!')

    if cnt<3: 
        print(f'{cnt}번 만에 맞춘 당신은 천재!')
    elif cnt<=6: 
        print(f'{cnt}번만에 맞추셨네요. 잘했어요^^')
    else: 
        print(f'{cnt}번 만에 맞추다니 쩝쩝...')

    
def print_stars():
    print('*'*10)
    
def print_stars_n(n):
    for _ in range(n): 
        print('*'*10)

def print_sum(a, b): 
    print(f'{a} + {b} = {a+b}')

def print_sub(a, b): 
    print(f'{a} - {b} = {a-b}')

def print_root(a, b, c): 
    det = b**2-4*a*c
    r1 = (-b-det**.5)/(2*a)
    r2 = (-b+det**.5)/2/a
    
    print(f'두 해: {r1:.1f}, {r2:.1f}')

def sum_range(a, b): 
    rslt = 0
    
    for x in range(a, b+1): 
        rslt += x
    
    print(f'{a} 이상 {b} 이하의 정수들의 합: {rslt}')
    

def function_call_test1(): 
    print_stars()
    print_stars_n(5) 

    print_sum(5,3)
    print_sub(5,3)
    
    print_root(2,-7,6)
    print_root(1,4,-21)
    print_root(1,0,9)
    
    sum_range(10, 20)
    
def circle_area_preim(r): 
    area = r*r*math.pi
    perimeter = 2*r*math.pi
    return area, perimeter 

def function_call_test2(): 
    print(circle_area_preim(3))
    a, p = circle_area_preim(3)
    print('원 넓이:', a)
    print('원 둘레 길이:', p)

    rslt = circle_area_preim(3) 
    print('원 넓이:', rslt[0])
    print('원 둘레 길이:', rslt[1])


def get_root(a, b, c): 
    det = b**2-4*a*c
    r1 = (-b-det**.5)/(2*a)
    r2 = (-b+det**.5)/2/a
    return r1, r2

def function_call_test3(): 
    x1, x2 = get_root(2,-7,6)
    print('작은 해:',x1)
    print('큰 해:',x2)
    
    