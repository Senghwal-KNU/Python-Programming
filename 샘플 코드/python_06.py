def sum_nums(*nums): 
    if len(nums)!=0: 
        avrg = sum(nums)/len(nums)
    else: 
        avrg = 0
    print(f'{len(nums)} 개의 인자 {nums}')
    print(f'합계: {len(nums)}, 평균 : {avrg}')
    
    
def sum_nums_test(): 
    sum_nums()
    sum_nums(10, 20, 30)
    sum_nums(10, 20, 30, 40, 50)
    
# sum_nums_test()

def min_nums(*nums): 
    if len(nums) == 0: 
        print('최솟값 없음')
        return 
        
    rslt = nums[0]
    
    for x in nums: 
        if rslt > x: 
            rslt = x
    
    print(f'최솟값은 {rslt}')
    
def min_nums_test(): 
    min_nums()
    min_nums(20, 40, 50, 10)
    
# min_nums_test()    

def str_test1(): 
    a = ['welcome', 'to', 'the', 'python', 'world']    
    first_a = [x[0] for x in a]
    print(first_a)
    
# str_test1()

def str_test2(): 
    st = 'Hello 1234 Python'
    #st에서 숫자만 모으기 
    lst = [int(x) for x in st if x.isdigit()== True]
    print(f"'{st}'에 포함된 수들의 합은 {sum(lst)}입니다.")

# str_test2()

def q11_16(): 
    test_list = ['No. 224', 'No. 587', 'No. 29', 'No. 37']
    
    lst = [int(x[4:]) for x in test_list]
    print(lst)
    
# q11_16()

def str_test3(): 
    while True: 
        msg = input('문장: ')
        
        lower_msg = msg.strip().lower()
        
        if lower_msg == 'quit': 
            print('프로그램을 종료합니다. ')
            break
            
        #알파벳만 소문자 버전으로 모은 리스트 생성 
        lst = [x for x in lower_msg if x.isalpha()]
        
        if lst == lst[::-1]: 
            print('회문입니다.')
        else: 
            print('회문이 아닙니다.')
            
        
# str_test3()

def lab5_12_1(): 
    print('_'.join('ABCD'))
        
# lab5_12_1()

def join_test1(): 
    msg = input('문장: ').split()
    print('불필요한 공백 제거 후:', ' '.join(msg))
        
    
# join_test1()        



def join_test2(): 
    lst = [int(x) for x in input('정수: ').split()]
    without_5 = [x for x in lst if x%5!=0]
    without_5_str = [str(x) for x in without_5]
    
    mul = 1
    for x in without_5: 
       mul *= x
        
    left_side = ' X '.join(without_5_str)
    
    print(f'{left_side} = {mul}')
# join_test2()    


def join_test3(): 
    n = int(input('양의 정수: '))
    pow_lst = [x**2 for x in range(1, n+1)]
    l_side = ' + '.join(f'{x}²' for x in range(1, n+1))
    
    print(f'{l_side} = {sum(pow_lst)}')
# join_test3()    