import random
import string

#import random 랜덤모듈
#random.randint(start,end): start~end 사이 정수형 난수
#random.randrange(start,end,step): range 내 정수형 난수
#random.random(): 0~1 실수형 난수

def random_test1():
    #=-10이상 10미만의 정수형 난수
    print(random.randint(-10,10))
    #=1이상 100이하의 짝수(정수) 난수
    print(random.randrange(2,101,2))
    #=0이상 5미만의 실수형 난수
    print(random.random()*5)
    #=-5이상 5미만의 실수형 난수*
    print(random.random()*10-5)
    #20이상 35미만의 실수형 난수
    print(random.random()*15+20)
# random_test1()

#random.choice(): 컬렉션 중 하나선택
#random.sample(어디서, 몇개): 컬렉션에서 중복없이 n개 선택
def random_test2():
    rslt=random.choice(string.ascii_lowercase)
    print(rslt)
    
    #가위, 바위, 보 중 하나 랜덤으로 출력
    rsp=['가위','바위','보']
    print(random.choice(rsp))
# random_test2()

#import string 문자열 메소드
#string.ascii_lowercase: 'abcd...' 문자열 상수
#string.ascii_uppercase: 'ABCD...' 문자열 상수
#string.punctuation: '...' 문자열 상수

def 랜덤모듈1():
    for _ in range(6):
        print(random.randint(0,9),end="")
    print()
    otp=''
    for _ in range(6):
        otp+=str(random.randint(0,9))
    print('otp ->',otp)
# 랜덤모듈1()

def 랜덤모듈2():
    #로또(1~45중 중복없이 6개)
    lotto=random.sample(range(1,45+1),6)
    print(lotto)
# 랜덤모듈2()

def 랜덤모듈3():
    import string
    a=string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits
    #pw1:중복문자 가능
    pw1=''
    for _ in range(8):
        pw1+=random.choice(a)
    print(pw1)
    #pw2:중복문자 불가
    pw2=random.sample(a,8)
    for s in pw2:
        print(s,end="")
    
    #특정 특수문자만..
    #비밀번호에 대소문자,숫자,특문이 다 포함되도록..
# 랜덤모듈3()

def 랜덤모듈4():
    # rnd=4
    rnd=random.randint(1,20)
    # print(rnd)
    cnt=0
    while True:
        ans=int(input("1~20까지의 숫자를 입력하세요: "))
        cnt+=1
        if rnd>ans:
            print(ans,"보다 큽니다!")
        elif rnd<ans:
            print(ans,"보다 작습니다!")
        elif rnd==ans:
            break
    if cnt<3:
        print(cnt,'번 만에 맞춘 당신은 천재!')
    elif cnt<7:
        print(cnt,"번만에 맞추셨네요. 잘했어요^^")
    else:
        print(cnt,'번 만에 맞추다니 쩝쩝...')
# 랜덤모듈4()

#정수 3개를 매개변수로 받아 세 수의 합 출력하는 함수
def sum_3int(a,b,c=0):
    print(f"{a}+{b}+{c}=",a+b+c)
# sum_3int(1,2)

def 함수1():
    def print_stars():
        print('*'*10)
    print_stars()
    
    def print_stars_n(n):
        for _ in range(n):
            print('*'*10)
    print_stars_n(3)
    
    def print_sum(a,b):
        print(f"{a}+{b}={a+b}")
    print_sum(1,2)
    
    def print_sub(a,b):
        print(f"{a}-{b}={a-b}")
    print_sub(1,2)
    
    def print_root(a,b,c):
        x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        print(f"두 해: {x1:.1f}, {x2:.1f}")
    print_root(2,-7,6)
    print_root(1,4,-21)
    print_root(1,0,9)
        
    def sum_range(a,b):
        rslt=0
        for x in range(a,b+1):
            rslt+=x
        print(f"{a} 이상 {b} 이하 정수들의 합: {rslt}")
    sum_range(10,20)
# 함수1()

def display_order(n,tf=True):
    if tf:
        print(f"햄버거 {n}개 찾아가세요.")
    else:
        print(f'양파 뺀 햄버거 {n}개 찾아가세요.')
# display_order(2)
# display_order(3, False)

def gen_hamburger(n,tf=True):
    if tf:
        return(f'햄버거 {n}개')
    else:
        return(f'양파 뺀 햄버거 {n}개')
# print(gen_hamburger(2))
# print(gen_hamburger(3,False))

def 함수2():
    def circle_area_preim(r): 
        area=str(r**2)+'pi' #import math
        preim=str(r*2)+'pi' #math.pi
        return area,preim
    print(circle_area_preim(3))
    
    def get_root(a,b,c):
        x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        return x1,x2
    x1,x2=get_root(2,-7,6)
    print(f'두 해: {x1:g}, {x2:g}')
    
    def sum_nums(*n):
        print(f'{len(n)} 개의 인자 {n}')
        print(f'합계 : {sum(n)} , 평균 : {sum(n)/len(n)}')
    sum_nums(10,20,30)
    sum_nums(10,20,30,40,50)
    
    def min_nums(*n):
        print("최솟값은",min(n))
    min_nums(20, 40, 50, 10)
# 함수2()

def 문자열_LAB():
    print('_'.join('ABCD'))
# 문자열_LAB()

def 문자열_메소드1():
    lst='one,two,three,four'.split(',')
    print(lst)
    for i in range(len(lst)):
        
    # print(lst[0][0])
문자열_메소드1()