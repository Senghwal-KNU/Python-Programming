import string 
import random
def palindrome_test(): 
    while True: 
        msg = input('문장: ').lower().strip()
        
        if msg == 'quit': 
            break
        
        for x in string.punctuation+' ': #메시지에서 구두점과 공백은
            msg = msg.replace(x, '') #빈 문자열로 교체
        
        if msg == msg[::-1]: 
            print('회문입니다.')
        else: 
            print('회문이 아닙니다.')
# palindrome_test()

def acronym_test(): 
    msg = input('문자열: ')
    #by, in, the, of, for, and 를 ' '로 변경하자. 
    #administration처럼 in이 포함된 단어는 변경하면 안됨. 
    #' in '과 같이 양 끝에 공백붙인 문자가 있다면 ' '로 변경하자.
        
    replace_lst = [' by ', ' in ', ' the ', ' of ', ' for ', ' and ']
    
    for x in replace_lst: 
        msg = msg.replace(x, ' ')
        
    lst = msg.split()
    
    acronym = ''.join([x[0].upper() for x in lst])
    print(acronym)
    
    
# acronym_test()
            
def expense_test():
    expense = input('오늘의 지출: ').replace('만원', '0000').replace('천원', '000')
    
    expense = [int(x) for x in expense.split()]
    
    print(f'총 {len(expense)}회 지출 총액은 {sum(expense):,}원이고, 회당 평균 지출은 {sum(expense)/len(expense):,.2f}원입니다.')

# expense_test()

def q11_16(): 
    test_list = ['No. 224', 'No. 587', 'No. 29', 'No. 37']
    lst = [int(x.replace('No.', '')) for x in test_list]

    print(lst)
    
# q11_16()
def q5_24(): 
    msg = input('문장: ')
    for x in string.punctuation:
        msg = msg.replace(x, ' ')

    lst = msg.split()
    print('사전식 정렬 후:', ', '.join(sorted(lst)))

# q5_24()
        
def twit_1_1(): 
    msg = input('메시지: ')
    
    print('단어 수:', len(msg.split()))

# twit_1_1()

def twit_1_2(): 
    msg = input('메시지: ')
    
    print("금지 단어 'foo' 수:", msg.count('foo'))

# twit_1_2()


def q5_26(): 
    msg = 'Park(Java city), Kim(C city), Kang(Bython city), Lee(Bython city), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++ city)'
    
    print(f'Bython이 {msg.count("Bython")}번 나옵니다.')

# q5_26()


def lab6_1(): 
    lst = list(range(2, 11, 2))
    print(lst)
    
    lst = 'Korea China India Nepal'.split() 
    print(lst)
    
    lst = list('xyz')
    print(lst)
    
# lab6_1()

def lab6_2(): 
    nations = 'Korea China Russia Malaysia'.split()
    print(nations[0])
    
    print(nations[-1])
# lab6_2()

def lab6_3(): 
    lst = [2,3,5, 7]
    lst.append(11)
    print(lst)
    
    lst.remove(3)
    print(lst)
    
    nations = 'Korea China Russia Malaysia'.split()
    nations.append('Nepal')
    print(nations)
    
    for x in ['Japan','Russia']: 
        if x in nations: 
            print(f'{x}는 국가 목록에 있습니다. ')
        else: 
            print(f'{x}는 국가 목록에 없습니다. ')
            
    print('사전에서 가장 먼저 나오는 나라:', min(nations))
    print('사전에서 가장 뒤에 나오는 나라:', max(nations))
    
    
# lab6_3()


def q6_4(): 
    lst = [2, 3, 4, 5, 6]
    rvs = []

    while True: 
        if len(lst)==0: 
            break

        rvs.append(lst.pop())
        
    print(rvs)
# q6_4()

def q6_17(): 
    animals = ['dog', 'cat', 'tiger', 'lion']
    
    for x in animals: 
        print(f'I love {x}.')
    
    animals.append(animals.pop(0))
    print('왼쪽 한 칸 로테이션:', animals)
    
    random.shuffle(animals)
    print('셔플 후:', animals)
    
    
# q6_17()
def q6_19(): 
    lst = ['abc', 'bcd', 'abc', 'abc', 'abba', 'cddc', 'opq', 'opq']
    rslt = []
    
    for x in lst: 
        if x not in rslt: 
            rslt.append(x)
    print(rslt)
    
# q6_19()


def list_method1(): 
    while True: 
        lst = input('과일 여러 개: ').split()
        if len(lst) > 0: 
            break
        else: 
            print('[입력오류] 과일을 입력해주세요.')
    
    rslt = []
    
    for x in lst: 
        if x not in rslt: 
            rslt.append(x)
    
    print('중복 제거 후 과일:', ', '.join(rslt))
    
    while True: 
        fruit = input('과일: ').strip()
        if fruit == '종료': 
            print('과일 추가 후:', ', '.join(rslt))
            break
        else: 
            rslt.append(fruit)
            print(f'{fruit}를 추가했습니다. ')
            
# list_method1()

def list_method2():   
    while True: 
        lst = input('과일 여러 개: ').split()
        if len(lst) > 0: 
            break
        else: 
            print('[입력오류] 과일을 입력해주세요.')
    
    rslt = []
    
    for x in lst: 
        if x not in rslt: 
            rslt.append(x)
    
    print('중복 제거 후 과일:', ', '.join(rslt))
    
    print('[과일 추가]')
    while True: 
        tmp = input('과일: ').strip()
        if tmp == '종료': 
            print('과일 추가를 종료합니다. ')
            break
        
        tmp = tmp.split()
        
        if tmp[0].isnumeric() == True: #첫 성분이 숫자라면
            idx = int(tmp[0])-1 #0번 성분은 인덱스
            tmp = tmp[1:] #1번 성분부터는 과일
            tmp = tmp[::-1] #역순으로 추가해야함
            
            for x in tmp: 
                rslt.insert(idx, x)
                    
        else: #첫 성분이 숫자가 아니면 
            rslt.extend(tmp)
                    
        print('과일 추가 후:', ', '.join(rslt))
# list_method2()

    

def list_method3(): 
    lst = []

    while True: 
        n = input('정수: ').strip().lower()

        if n == 'stop': 
            break

        n = int(n)    
        if n%2==0: 
            lst.append(n)
            
    if len(lst)>0: 
        print(f'입력 값 중 짝수들:', ', '.join([str(x) for x in lst]))
    else: 
        print('입력 값 중에는 짝수가 없습니다.')

# list_method3()
        
def list_method4_1(): 
    msg = input('오늘의 지출: ').split()
    lst = []
    
    for x in msg: 
        if '만원' in x: 
            money = x.replace('만원', '')
            money = float(money)*10000
        elif '천원' in x: 
            money = x.replace('천원', '')
            money = float(money)*1000
        else: 
            money = float(x)
        
        lst.append(money)
    
    print('총 {}회 지출 총액은 {:,}원이고, 회당 평균 지출은 {:,}원입니다.'.format(len(lst), sum(lst), sum(lst)/len(lst)))
    
# list_method4_1()
def list_method5(): 
    tmp = input('문자열: ').split()
    rmv = 'by in the of for and'.split()
    #rmv = ['by', 'in', 'the', 'of', 'for', 'and']
    
    lst = []
    for x in tmp: 
        if x not in rmv: 
            lst.append(x)
            
    acr = ''.join([x[0].upper() for x in lst])
    print(acr)  
        
        
# list_method5()