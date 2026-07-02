def in_range_even(): 
    num = int(input('정수: '))
    print('입력된 정수는 0에서 100 사이에 있는 짝수입니다:', 0<num<100 and num%2==0)
    print('입력된 정수는 0에서 100 사이에 있는 짝수입니다:', num in range(2, 100, 2))

def rev_num(): 
    num = int(input('세 자리 정수: '))

    digit1 = num%10
    digit10 = (num%100)//10
    # digit10 = num//10%10
    digit100 = num//100
    
    print('1의 자리 숫자:', digit1)
    print('10의 자리:', digit10)
    print('100의 자리:', digit100)

    print(digit1, digit10, digit100, sep = '')
 
def age_test(): 
    age = int(input('나이: '))

    if age<20: 
        print('청소년 할인되었습니다.')
    print('입장하세요.')

def walk_test(): 
    walk_cnt = int(input('걸음 수: '))

    if walk_cnt>=1000: 
        print('목표 달성')

def time_test1(): 
    time = int(input('시간: '))

    if 0<=time<12:
        print('오전입니다.')
    elif 12<=time<24: 
        print('오후입니다.')
    else: 
        print('[입력오류] 시간은 0 이상 24 미만의 값으로 입력해주세요. ')
        

def time_test2(): 
    time = int(input('시간: ')) 
    
    if time not in range(24): 
        print('[입력오류] 시간은 0이상 24미만의 값으로 입력해주세요. ')
    elif time<12: 
        print('오전입니다.')
    else: 
        print('오후입니다.')

def vel_test(): 
    vel = float(input('속도: '))
    
    if vel<0 or vel>=150: 
        print('[입력오류] 속도는 0 이상 150 미만의 값만 가능합니다.')
    elif vel>=100: 
        print('고속')
    elif vel>=60: 
        print('중속')
    else: 
        print('저속') 
        
def score_test(): 
    score = int(input('점수: '))
    
    if score not in range(101): 
        print('[입력오류] 점수는 0 이상 100 이하의 값만 가능합니다.')
    elif score>=90: 
        print('A')
    elif score>=80: 
        print('B')
    elif score>=70: 
        print('C')
    elif score>=60: 
        print('D')
    else: 
        print('F') 
        
        
def age_height_test(): 
    age = int(input('나이: '))
    height = float(input('키: '))

    if age>=19 and height>=150:
        print('입장할 수 있습니다.')
    else: 
        print('입장할 수 없습니다.')


def moeum_test(): 
    usr = input('알파벳: ')

    if usr in 'aeiouAEIOU': 
        rslt = '모음'
    else: 
        rslt = '자음'

    print(f'{usr}(은)는 {rslt}입니다.')
    #rslt가 조건문에서 선언되었지만 같은 함수안에서 정의 되었기 때문에 접근 가능

def month_test(): 
    year, month = [int(x) for x in input('년도, 월 (콤마로 구분하여 입력): ').split(',')] #[2026,3]

    if month<1 or month>12: #if month  not in range(1, 13): 
        print('[입력 오류]1월 ~ 12월만 존재합니다.')
        return #아래 코드 실행하지 말자! = 이 함수 종료하자!!
    elif month == 2: 
        if year %4 ==0 and year%100!=0 or year%400==0: 
            days = 29
        else: 
            days = 28
    elif month in [4, 6, 9, 11]: #'4, 6, 9, 11'안됨. 
        days = 30  
    else: 
        days = 31

    print(f'{year}년 {month}월은 {days}일까지 존재합니다.')

   

def classify_chr(): 
    usr = input('문자: ')
    
    if usr.isnumeric():# == True:
        rslt = '숫자'
    #elif usr가 영어알파벳이라면:
    # elif usr.isalpha(): #한글도 True이기 때문에 이걸로는 부족
    # elif usr.isalpha() and usr.isascii(): #좋음: 영어 문자만 걸러냄
    elif 'a'<=usr<='z' or 'A'<=usr<='Z': 
        if usr in 'aeiouAEIOU':
            rslt = '모음'
        else: 
            rslt = '자음'
    else: 
        rslt = '기타문자'
    print(f'{usr}는 {rslt}입니다.')