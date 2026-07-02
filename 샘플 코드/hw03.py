def q3_6(): 
    a, b, c = [int(x) for x in input('정수 세 개: ').split()]
    
    #우선 제일 작은 수를 a에 
    if a>b:
        a, b = b, a
    if a>c: 
        a, c = c, a
        
    #b,c 정렬
    if b>c: 
        b, c = c, b

    print(a, b, c)


def q3_8(): 
    x, y = [float(x) for x in input('점의 좌표 x  y: ').split()]
    
    if x>0 and y>0:
        print('1사분면')
    elif x>0 and y<0:
        print('4사분면')
    elif x<0 and y>0:
        print('2사분면')
    elif x<0 and y<0:
        print('3사분면')
    elif x==0 and y==0:
        print('원점')
    elif x==0:
        print('y축')
    else: 
        print('x축')
        
def q3_9(): 
    num = int(input('정수를 입력하시오 : '))
    
    if num % 2 == 0:
        print(num,'(는)은 2(으)로 나누어집니다.')
    else:
        print(num,'(는)은 2(으)로 나누어지지 않습니다.')

    if num % 3 != 0:
        print(num,'(는)은 3(으)로 나누어지지 않습니다.')
    else:
        print(num,'(는)은 3(으)로 나누어집니다.')

    if num % 2 == 0 and num % 3 == 0:
        print(num,'는(은) 2와(과) 3 모두로 나누어집니다.')
    else:
        print(num,'는(은) 2와(과) 3 모두로 나누어지지 않습니다')

def q2_22(): 
    a = int(input('a: '))
    b = int(input('b: '))
    print('a를 b로 나눈 몫:', a//b)
    print('a를 b로 나눈 나머지:', a%b)
    
def q3_4(): 
    age = int(input('나이: '))
    if age>=20:
        print('Adult')
    elif age>=10:
        print('Youth')
    else: 
        print('Kid')
    
def q3_10(): 
    a, b = [int(x) for x in input('두 정수: ').split()]
    if a%b==0: 
        print(f'{a}는 {b}의 배수입니다.')
    else: 
        print(f'{a}는 {b}의 배수가 아닙니다.')
    
    
def q3_11(): 
    usr = [int(x) for x in input('세 복권번호: ').split()]
    cnt = 0
    
    #당첨번호 2,3,9가 사용자 입력값에 포함되어 있는지 확인 
    
    if 2 in usr: #사용자 입력 값에 2가 있다면
        cnt+=1 #cnt 하나 증가 
    if 3 in usr: #elif 가 아니라 독립적인 if문 사용자
        cnt+=1
    if 9 in usr: #elif 가 아니라 독립적인 if문 사용자
        cnt+=1
        
    if cnt==3: 
        print('상금 1억원')
    elif cnt==2: 
        print('상금 1천만원')
    elif cnt==1: 
        print('상금 1만원')
    else: 
        print('다음 기회에...')
        
def min_to_max():
    nums = [int(x) for x in input('정수 여러 개: ').split(',')]
    _min = min(nums)
    _max = max(nums)

    print(f'{_min} 이상 {_max} 이하 정수들의 합: {sum(range(_min, _max+1))}')

def min_to_max2(): 
    nums = [int(x) for x in input('정수 여러 개: ').split(',')]
    _min = min(nums)
    _max = max(nums)

    print(f'{_min} 초과 {_max} 미만 정수들의 합: {sum(range(_min+1, _max))}')

def min_to_max_expt_usr(): 
    nums = [int(x) for x in input('정수 여러 개: ').split(',')]
    _min = min(nums)
    _max = max(nums)

    target = [x for x in range(_min+1, _max) if x not in nums]
    print(f'{_min} 초과 {_max} 미만 정수들의 합(사용자 입력 값 제외): {sum(target)}')

def feet_inch(): 
    height = float(input('키: '))
    
    inch = height/2.54
    
    feet = inch//12
    res_inch = inch%12
    
    print(f'{height:.2f}cm는 {feet:.2f}피트 {res_inch:.2f}인치입니다.')
    
    
def str_method_test(): 
    msg = input('문장: ')
    
    rslt = [x for x in msg if x.isdigit()]
    print('문장에 포함된 숫자:',rslt)
    
    rslt = [int(x) for x in msg if x.isdigit()]
    print('문장에 포함된 숫자 총합:',sum(rslt))
    
    
    rslt = [x for x in msg if x.isspace()]
    print('문장에 포함된 공백:', rslt)
    print('문장에 포함된 공백 개수:', len(rslt))
    
    rslt = [x for x in msg if x in 'aeiouAEIOU']
    print('문장에 포함된 모음:', rslt)
    print('문장에 포함된 모음 개수:', len(rslt))
    
    rslt = [x for x in msg if x.islower()]
    print('문장에 포함된 소문자:', rslt)
    print('문장에 포함된 소문자 개수:', len(rslt))    
    
    
def digit100_test(): 
    num = int(input('양의 정수: '))
    if num<0: 
        print('[입력오류] 양의 정수를 입력해주세요. ')
    else: 
        digit100 = num//100%10
        # digit100 = num%1000//100
        
        print('백의 자리 숫자:', digit100)
        
        
def digit_test(): 
    num = int(input('양의 정수: '))
    target = int(input('확인할 자리:'))
    
    if num<0: 
        print('[입력오류] 양의 정수를 입력해주세요. ')
    else: 
        digit = num //target %10
        # digit = num %(target*10)//target
        print(f'{target}의 자리수:', digit)
    
        