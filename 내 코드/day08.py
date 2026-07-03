#python_07 실습코드 내용
def list_method_6_19():
    lst = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
    rslt=[]
    for i in lst:
        if i not in rslt:
            rslt.append(i)
    print(rslt)
# list_method_6_19()

def list_method_1():
    #입력
    while True:
        fruits=input("과일 여러 개: ").split()
        if len(fruits)==0:
            print('[입력오류] 과일을 입력해주세요.')
        else:
            break
            
    #중복 제거
    fruits_new=[]
    for x in fruits:
        if x not in fruits_new:
            fruits_new.append(x)
    print('중복 제거 후 과일:',fruits_new)
    
    #문제 1.2
    while True:
        fruit=input("과일: ").strip()
        if fruit=='종료':
            break
        else:
            print(fruit+'를 추가했습니다.')
            fruits_new.append(fruit)
    print('과일 추가 후:',', '.join(fruits_new))
# list_method_1()

def list_method_6_4():  #pop(), append() 사용
    lst=[2,3,4,5,6]
    rvs=[]
    for x in range(len(lst)):
        rvs.append(lst.pop())
    print(rvs)
# list_method_6_4()

def list_method_6_17():
    #3) animals 리스트 왼쪽 로테이션, 리스트 메소드 사용
    animals='dog,cat,tiger,lion'.split(',')
    animals.append(animals.pop(0))
    print('animals =',animals)
# list_method_6_17()

def list_method_6_17_r():
    #3) animals 리스트 오른쪽 로테이션, 리스트 메소드 사용
    animals='dog,cat,tiger,lion'.split(',')
    animals.insert(0,animals.pop())
    print('animals =',animals)
# list_method_6_17_r()

def list_method_2():
    #입력
    while True:
        fruits=input("과일 여러 개: ").split()
        if len(fruits)==0:
            print('[입력오류] 과일을 입력해주세요.')
        else:
            break
            
    #중복 제거
    fruits_new=[]
    for x in fruits:
        if x not in fruits_new:
            fruits_new.append(x)
    print('중복 제거 후 과일:',', '.join(fruits_new))
    
    print('------------------------------------')
    print("[과일 추가]\n")
    
    while True:
        fruits_extend=input('과일: ').strip().split()
        if fruits_extend[0]=='종료':
            print('과일 추가를 종료합니다.')
            break
        if fruits_extend[0].isdigit(): #숫자포함
            n=int(fruits_extend.pop(0))-1
            for x in fruits_extend:
                if x not in fruits_new:
                    fruits_new.insert(n,x)
                    n+=1
            print('과일 추가 후:',', '.join(fruits_new))
        else: #숫자없음
            for x in fruits_extend:
                if x not in fruits_new:
                    fruits_new.append(x)
            print('과일 추가 후:',', '.join(fruits_new))
# list_method_2()

#python_08 실습코드 내용

#/////////////////////////////////////////////////////////////////

#튜플 tp=(1,2,3,..)

#튜플 생성1: 원소나열
#튜플 생성2: 캐스팅
#튜플 생성3: *튜플 축약*
# tp=tuple(x for x in lst if x%2!=0) #←처럼 tuple()로 캐스팅해줘야 함

#튜플 메소드
    # count(x)
    # index(x)

#/////////////////////////////////////////////////////////////////

#집합(set) s={1,2,3,..}
#순서무관(인덱스x),중복불가

#*공집합 생성*
#s=set()    *s=set{}으로 하면 dict이 됨

#셋 생성1: 원소나열
#셋 생성2: 캐스팅
#셋 생성3: *셋 축약*
# s=set(range(0,10,2))
def set축약():
    s2=set(range(0,10,2))
    print(s2)
    s={'no. '+str(x) for x in s2}
    print(s)
# set축약()

#집합연산 가능
    # 합집합     a.union(b) a|b
    # 차집합     a.difference(b) a-b
    # 교집합     a.intersection(b) a&b
    # 대칭차집합   a.symmetric_difference(b) a^b
    # 부분집합    a.issubset(b)
    # 상위집합    a.issuperset(b)
    # 서로소     a.isdisjoint(b)

#집합 메소드
    # 추가      s.add(x)
    # 삭제      s.discard(x)
    # 모두삭제    s.clear()
    
def 강의자료case1(): 
    str1='Hello, world!'
    str2='how are you?'
    #공통 문자, 문자열1에만 출현한 문자 출력
    str1=str1.lower()
    str2=str2.lower()
    
    s1={x for x in str1 if x.isalpha()}
    s2={x for x in str2 if x.isalpha()}
    
    print('공통 문자:',s1&s2)
    print('문자열1에만 출현한 문자(알파벳):',s1-s2)
# 강의자료case1()

def 강의자료case2():
    st='Apple: "Papa!"'
    #출현한 알파벳만 출력(중복 없이)
    st=st.lower()
    
    s1=set(st)
   
    print('출현한 알파벳:',s1&s2)
# 강의자료case2()

#tuple, set -> 3번
#set -> 모두
#tuple 7.7~10

def p3():
    usr=input('문자열: ').lower()
    s1={x for x in usr if x.isalpha()}
    lst1=list(s1)
    lst1.sort()
    print('출현한 알파벳:',' '.join(lst1))
# p3()

# def p7_18():
    # 7.18 다음 코드의 수행 결과를 적으시오. 이 중에서 에러가 발생하는 부분은 어느 부분인가?
    # ```
    # >>> s1 = set('abcd')
    # >>> s1
    # (1) {'a', 'b', 'd', 'c'}
    # >>> s2 = set('defg')
    # >>> {'e', 'g', 'd', 'f'}
    # (2) {defg}
    # >>> s1 == s2
    # (3) False
    # >>> s1 + s2
    # (4) 에러: set는 + 사용 불가
    # >>> s1 & s2
    # (5) {'d'}
    # ```

# def p7_19():
    # 7.19 다음과 같은 집합에 대한 연산을 적용할 적에, 다음 밑줄 친 부분에 들어갈 알맞은 결과는 무엇인가?
    # ```
    # >>> s1 = {0, 1, 2, 3, 4, 5}
    # >>> s2 = {3, 4, 5, 6, 7}
    # >>> s1 & s2
    # (1) {3, 4, 5}
    # >>> s1 | s2
    # (2) {0, 1, 2, 3, 4, 5, 6, 7}
    # >>> s2 - s1
    # (3) {6, 7}
    # >>> s1 - s2
    # (4) {0, 1, 2}
    # >>> s1 ^ s2
    # (5) {0, 1, 2, 6, 7}
    # >>> 2 in s1
    # (6) True
    # ```

# def pset1():
    # set1. 두 개의 세트가 아래와 같이 주어져 있을 때 아래에 답하시오.
    # ```
    # 첫 번째 세트 {10, 20, 30, 40, 50, 60}
    # 두 번째 세트 {30, 40, 50, 60, 70, 80}

    # 어느 한 쪽에만 있는 원소 {10, 20, 70, 80}
    # 첫 번째 세트^두 번째 세트

    # 첫 번째에만 있는 원소 {10, 20}
    # 첫 번째 세트-두 번째 세트
    # ```

def p7_7():
    tup1=(100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
    print('일일 매출 기록',tup1)
    cnt=0 
    for i in range(1,len(tup1)):
        if tup1[i-1]>tup1[i]:
            cnt+=1
    print(f'지난 10일 동안 전일대비 매출이 감소한 날은 {cnt}일입니다.')
# p7_7()

def p7_8():
    tup1=(1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)
    print('주어진 튜플은:',tup1)
    set1=set()
    for x in tup1:
        if tup1.count(x)>1:
            set1.add(x)
    s={x for x in tp if tup1.count(x)>1}
    
    # print('중복 원소는:',)
# p7_8()

def p7_9():
    tup1=(1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)
    tup1=tuple(set(tup1))
    print('중복 제거 튜플:',tup1)
# p7_9()

def p7_10():
    tup1=(1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
    tup2=(1, 2, 5, 4, 3, 2, 9, 4, 7, 8, 9, 9, 3, 7, 3)
    
    def freq_elt(tup):
        cnt=0
        lst=[]
        #s=set(tup)
        for x in tup: #tup 대신 s쓰면 반복 줄일 수 있음   
            if tup.count(x)>cnt:
                cnt=tup.count(x)
                lst=[]
                lst.append(x)
            elif tup.count(x)==cnt:
                lst.append(x)
        lst.sort()
        n=lst[-1]
        return n
    print('가장 많이 나타나는 원소는:',freq_elt(tup2))
p7_10()