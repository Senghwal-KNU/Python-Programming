def tel_nbr_test(): 
    while True: 
        nbr = input('휴대전화번호: ').strip()
        
        err_flag = 0
        if len(nbr) not in range(10, 12):
            err_flag += 1
            print('[입력오류] 전화번호는 10자리 혹은 11자리로 구성되야 합니다.')
            
        if nbr.isdigit() == False:
            err_flag += 2
            print('[입력오류] 전화번호는 숫자로만 입력해주세요.')
            
        if nbr[:3] != '010':
            err_flag += 4
            print('[입력오류] 전화번호는 010으로 시작해야 합니다.')
            
        if err_flag == 0: 
            break
    
    print(f'입력하신 번호는 010-{nbr[3:-4]}-{nbr[-4:]}입니다.')
            
# tel_nbr_test()

def ispy(f_name): #slicing 버전
    ext = f_name.strip()[-3:] # 이 경우 맨 마지막 3문자가 '.py'인지 확인해야 함. 
    if ext == '.py': 
        return True
    else: 
        return False
        

def ispy2(f_name): #split()버전
    ext = f_name.split('.')[1] #.을 기준으로 분리해 확장자가 py인지 확인 
    rslt = False #우선은 결과를 False로 둠
    
    if ext == 'py': #확장자가 py이면 
        rslt = True #결과를 True로 변경 
        
    return rslt


def py_test(): 
    file_name = input('파일명: ')
    
    if ispy(file_name): 
        print('파이썬 소스파일입니다.')
    else: 
        print('파이썬 소스 파일이 아닙니다.')
    
# py_test()
    
def py_test2():
    file_name = input('파일명: ')
    
    if ispy2(file_name): 
        print('파이썬 소스파일입니다.')
    else: 
        print('파이썬 소스 파일이 아닙니다.')
# py_test2()

def common_mul_lst(num1, num2, div1, div2): 
    rslt = [x for x in range(num1, num2+1) if x%div1==0 and x%div2 == 0]
    
    return rslt
    
def q11_10():
    n1 = int(input('정수 1: '))
    n2 = int(input('정수 2: '))
    
    if n1>n2: 
        n1, n2 = n2, n1
        
    print(f'{n1} 이상 {n2} 이하의 수에서 x, y의 공배수를 구합니다. x, y를 입력해주세요. ')
    
    x = int(input('x: '))
    y = int(input('y: '))
    
    rslt = common_mul_lst(n1, n2, x, y)
    str_ver = [str(x) for x in rslt]
    
    print('공배수:', ', '.join(str_ver))
    
    
    
# q11_10()



def q11_12():
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    rslt = [x[:3].upper() for x in days]
    
    print(rslt)
    
# q11_12()


def q5_21(): 
    while True: 
        nbr = input('주민등록번호: ')
        if nbr.isnumeric() == True: 
            break
        else: 
            print('[입력 오류] 숫자로만 입력해주세요.')
        
    year = int(nbr[:2])
    month = int(nbr[2:4])
    day = int(nbr[4:])
    
    if year>=50: 
        year += 1900
    else: 
        year += 2000
        
    print(f'{year}년 {month}월 {day}일')
    
    
# q5_21()    


def q6_7(): 
    lst = [10, 20, 30, 50, 60]
    s = 0
    for x in lst: 
        s += x
    
    print('원소들의 합:',s)
    
# q6_7()

def q6_9(): 
    lst = [10, 20, 30, 50, 60]
    
    max_lst = lst[0]
    
    for x in lst: 
        if x>max_lst: 
            max_lst = x
    
    print('최댓값:', max_lst)

# q6_9()

def q6_12(): 
    n = int(input('n: '))
    
    while True: 
        lst = [int(x) for x in input(f'{n}개의 수: ').split()]
        if len(lst) == n: 
            break
        else: 
            print(f'[입력 오류] {n}개의 수를 입력해주세요.')
    
    print('합:', sum(lst))
    print('평균:', sum(lst)/len(lst))
    print('최댓값:', max(lst))
    print('최솟값:', min(lst))
    
# q6_12()

def q6_13(): 
    lst = [int(x) for x in input('정수들: ').split()]
    
    print('합:', sum(lst))
    m = sum(lst)/len(lst)
    print('평균:', m)
    sq_dev = [(x-m)**2 for x in lst]
    
    print('표준편차:', (sum(sq_dev)/len(lst))**.5)
  
# q6_13()

def how_many_persons(lst): 
    return len(lst)//5

def compute_average_age(person_list): 
    ages = person_list[1::5] #[20, 25, 22, 40]
    return sum(ages)/len(ages)

def count_males_females(person_list): 
    genders = person_list[2::5]
    
    #남자 : 1, 여자 : 0
    male_cnt = sum(genders)
    female_cnt = len(genders)- sum(genders)
    return male_cnt, female_cnt

def display_persons(person_list):
    n = how_many_persons(person_list)

    for i in range(n): 
        print(person_list[5*i:5*(i+1)])

def q5_23(): 
    person1 = ['온달', 20, 1, 180.0, 100.0]
    person2 = ['이사부', 25, 1, 170.0, 70.0]
    person3 = ['평강', 22, 0, 169.0, 60.0]
    person4 = ['혁거세', 40, 1, 150.0, 50.0]

    person_list = person1 + person2 + person3 + person4

    n_persons = how_many_persons(person_list)
    print(f'{n_persons}명의 정보가 담겨 있습니다.')

    average_age = compute_average_age(person_list)
    print(f'평균 나이는 {average_age}세입니다.')

    rslt = count_males_females(person_list)
    print(f'리스트에는 남자가 {rslt[0]}명, 여자가 {rslt[1]}명입니다.')

    display_persons(person_list) 
    
# q5_23()