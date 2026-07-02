#양의 정수 n 입력 받음->n 이상의 소수 한 개 출력
def prime_n():
    n=int(input("양의 정수 입력: "))
    while True:
        for x in range(2,n):
            if n%x==0:
                n+=1
                continue
            break
        break
    print("결과 :",n)
# prime_n()

def sum_nums(*n):
    print(f"{len(n)} 개의 인자",n)
    print(f"합계 : {sum(n)}, 평균 : {sum(n)/len(n)}")
# sum_nums(10,20,30)
# sum_nums(10,20,30,40,50)

def min_nums(*n): #내장함수 사용하지 말 것
    rslt=n[0]
    for i in n:
        if i<rslt:
            rslt=i
    print('최솟값은',rslt)
# min_nums(20,40,50,10)
# min_nums(-11.4,7.8,9.5,2.1,1.3)

def str_method_1(): #첫 알파벳 추출한 리스트
    a=['welcome','to','the','python','world']
    first_a=[]
    for i in range(len(a)):
        first_a.append(a[i][0])
    print("first_a =",first_a)
# str_method_1()

def str_method_2(): #한자리 숫자 리스트로 만들어서 합 구하기..
    st='Hello 1234 Python'
    st_num=[]
    for i in st:
        if i.isdigit():
            st_num.append(i)
    rslt=0
    for i in st_num:
        rslt+=int(i)
    print(f"'{st}'에 포함된 수들의 합은 {rslt}입니다.")
# str_method_2()

def str_method_11_11(): #첫글자 대문자로 만들기..
    lst='one,two,three,four'.split(",")
    def use_slicing():
        rslt=[]
        for i in range(len(lst)):
            tmp=''
            tmp+=(lst[i][:1].upper())
            tmp+=(lst[i][1:])
            print(tmp)
            rslt.append(tmp)
        print(rslt)
    def use_method():   #.capitalize(문자열의 문장 첫글자 대문자로), .title(문자열 각 단어의 첫글자 대문자로)
        pass
    def 리스트축약():
        rslt=[x[0].upper()+x[1:] for x in lst]
        print(rslt)
    # 리스트축약()
# str_method_11_11()

def str_method_11_16(): #No. 제외한 숫자를 정수리스트로..
    test_list = ['No. 224', 'No. 587', 'No. 29', 'No. 37']
    num_list=[int(x[4:]) for x in test_list]
    print(num_list)
# str_method_11_16()

def str_method_3():
    while True:
        st=input('문장: ')
        if 'quit' in st.lower():
            print("프로그램을 종료합니다.")
            break
        st_alp=[x.lower() for x in st if x.isalpha()]
        if st_alp==st_alp[::-1]:
            print("회문입니다.")
        else:
            print('회문이 아닙니다.')
str_method_3()

def LAB_5_12_1():
    print('_'.join('ABCD'))
# LAB_5_12_1()

def join_1():
    st=input("문장: ").split()
    print(' '.join(st))
# join_1()

def join_2():
    nums=[n for n in input("정수: ").split() if int(n)%5!=0]
    # print(nums)
    # print(' X '.join(nums))
    rslt=1
    for i in nums:
        rslt*=int(i)
    print(' X '.join(nums),"=",rslt)
# join_2()

def join_3():
    n=int(input("양의 정수: "))
    rslt=0
    lst=[]
    for i in range(1,n+1):
        lst.append(str(i)+'²')
        rslt+=i**2
    print('+'.join(lst),"=",rslt)
    
    print('+'.join([str(x)+'²' for x in range(1,n+1)]),"=",rslt)
# join_3()

def replace_test():
    st='hello world'
    st=st.replace('o','O')
    print(st)
# replace_test()

