def key_test():
    #sorted(), min(), max() 내장함수와 key 인자 전달

    scores = '83 47 29 66 53 73 61 21 9 2'.split()

    print(max(scores))

    #정수 기준 최댓값 | int()함수를 키로..
    print('scores 최댓값:',max(scores,key=int))

    #정수로 볼때 최댓값
    nums = [70, 58, 13, 46, -21, -89, 86, -28, -60, -79]
    print('nums 최댓값:',max(nums))

    #절댓값 기준 최댓값 | abs()함수를 키로..
    print('절댓값 기준 최댓값',max(nums,key=abs))

    #a가 가장 많이 포함된 성분
    st='abc aaabb zsjwuiqqq aaaaa'.split()
    print(st)
    # print(max(st,key=str.count(성분,'a'))) # 에러 발생
# key_test()

def lambda_test():
    # 기존함수로 key 표현 어려울 때?
    # => 람다함수 사용
    print(max(st,key=lambda x:x.count('a')))

    #lambda 함수: 한 줄짜리 간단한 함수, 익명함수
    #lambda 매개변수: 반환값
    def add(a,b):
        return a+b
    # 위아래 같은 함수
    lambda a,b:a+b
    c=(lambda a,b:a+b)(3,4)
    print(c)

    #세 개의 수를 매개변수로 받아 세 수의 곱을 반환하는 람다함수
    lambda a,b,c:a*b*c
    print((lambda a,b,c:a*b*c)(2,3,4))
    #문자열을 매개변수로 받아 'a'의 개수를 반환하는 람다함수
    lambda st:st.count('a')
    print((lambda st:st.count('a'))('abcadsdfaadfada'))
    #리스트를 매개변수로 받아 마지막 성분을 반환하는 람다함수
    lambda lst:lst[-1]
    print((lambda lst:lst[-1])(st))
# lambda_test()

def q_10_3():
    persons = [('GilDong', 'Hong', 27), ('SunSin', 'Lee', 46), ('YuSin', 'Gim', 34)]  
    print('나이순 정렬',sorted(persons, key=lambda info: info[2]))
    print('성씨순 정렬',sorted(persons, key=lambda info: info[1]))
    print('나이순(내림차순) 정렬',sorted(persons, key=lambda info: info[2], reverse=True))
# q_10_3()

def q_1():
    coordinates = [(1.2, 3.4), (5.6, 7.8), (9.0, 1.1), (2.2, 4.4), (6.6, 8.8), (0.5, 3.3), (7.7, 2.1)]
    print('원점으로부터 먼 점부터 정렬한 결과:')
    print(sorted(coordinates, key=lambda t:(t[0]**2+t[1]**2)**0.5,reverse=True))
# q_1()

def q_2():
    coordinates = [(1.2, 3.4), (5.6, 7.8), (9.0, 1.1), (2.2, 4.4), (6.6, 8.8), (0.5, 3.3), (7.7, 2.1)]
    print('원점과 연결했을 때 기울기가 가장 작은 점:',min(coordinates,key=lambda t:t[1]/t[0]))
# q_2()

def q_3():
    lst = ['alpha12beta34', 'gamma', 'delta56epsilon7', 'zeta', 'theta89', 'iota3kappa2lambda', 'mu', 'nu45xi', 'omicronpi', 'rho77sigma1']
    
    print('문자열에 포함된 수들의 합이 가장 큰 문자열:',max(lst,key=lambda st:sum(int(n) for n in st if n.isdigit())))
# q_3()

# 소모성: zip(), 파일
# 소모성 있는 형식의 특징: next()를 통해 접근 가능

#hw13
#scores.csv->학생별 점수 딕셔너리 생성
def hw13_1():
    import csv
    dct={}
    with open('scores.csv','rt') as f:
        parsed=csv.reader(f)
        next(f) # 헤더 날리기
        next(f) # 헤더 날리기
        # dct={x[0]:tuple(int(n) for n in x[1:]) for x in parsed}
        for x in parsed:
            dct[x[0]]=tuple(int(n) for n in x[1:])
    print(dct)
    print(sorted(dct)) # key(이름) 기준으로 정렬됨
    # 총점순으로 정렬하고파(내림차순)
    print(sorted(dct,key=lambda x:sum(dct[x]),reverse=True))
    
#C++(마지막 성분) 최고 성적자 3명 출력
#max 대신 sorted로 정렬 -> 3명 추리기
#print(이름, 성적)
    print('C++ 최고 성적자 3명')
    cpp_top3=sorted(dct, key=lambda x:dct[x][-1],reverse=True)[:3]
    for x in cpp_top3:
        print(f'{x}: {dct[x][-1]}점')

#java 성적 최고점자 출력
    print('java 최고 성적자')
    java_top1=max(dct,key=lambda x:dct[x][-2])
    print(f'{java_top1}: {dct[java_top1][-2]}점')
    # 근데 동점자가 있는데 1명만 나오는데??

#java 성적 최고점자(동점시 둘다 출력)
    # print('java 최고 성적자(동점 반영)')
    # java_sorted=sorted(dct, key=lambda x:dct[x][-2],reverse=True)
# hw13_1()

def hw13_student():
    class Student: 
        def __init__(self, name, py, cpp): 
            self._name = name
            self._py = py
            self._cpp = cpp
        
        def __str__(self): 
            return f'파이썬 {self._py}점, C++ {self._cpp}점인 {self._name} 학생입니다. '
            
        def __repr__(self): 
            return f'<{self._name} - 파이썬: {self._py}점, C++: {self._cpp}점>'
        
        def get_total(self):    
            return self._py+self._cpp

        def __ge__(self, other): 
            return self.get_total()>=other.get_total()
        def __lt__(self, other): 
            return self.get_total()<other.get_total()
            
        def get_name(self): 
            return self._name
        
        def get_py(self):
            return self._py
    
    import csv
    
    def student_test2(): 
        with open('scores.csv', 'rt') as f: 
            parsed = csv.reader(f)
            next(parsed)
            next(parsed)
            # 학생 객체 리스트 생성 1: 리스트 축약
            lst = [Student(x[0], int(x[2]), int(x[4])) for x in parsed]
            
            # 학생 객체 리스트 생성 2: 객체 생성 후 리스트에 하나씩 추가
            # lst = []
            # for x in parsed:
                # name, _, py, _, cpp = x #unpackin 이 방식은 아래와 같이 리스트 축약에서도 사용 가능
                # std = Student(name, int(py), int(cpp)) 
                # lst.append(std)
                
                
            # 학생 객체 리스트 생성 3: 리스트 축약과 언패킹 조합 
            # lst = [Student(name, int(py), int(cpp))  for name, _, py, _, cpp in parsed]
        print(lst)
    # student_test2() 
    
    def student_test3(): 
        with open('scores.csv', 'rt') as f: 
            parsed = csv.reader(f)
            next(parsed)
            next(parsed)
            lst = [Student(x[0], int(x[2]), int(x[4])) for x in parsed]
            
        print(f'{lst[0].get_name()}의 총점 >= {lst[1].get_name()}의 총점:', lst[0]>=lst[1])
        
        print('총점 순 내림차순 정렬:', sorted(lst, reverse = True))
        highest = max(lst)
        print(f'최고득점자: {highest.get_name()}(총점 {highest.get_total()}점)')    
    # student_test3()
    
    #파이썬 최고점자 5명 출력
    #__lt__ 바꾸기는 위험
    #일시적
    def student_pytop5():
        with open('scores.csv','rt') as f:
            parsed = csv.reader(f)
            next(parsed)
            next(parsed)
            lst=[Student(x[0],int(x[2]),int(x[4])) for x in parsed]
        pytop5=sorted(lst,reverse=True,key=Student.get_py)[:5] #파이썬 최고점자 5명 리스트
        print(pytop5)
    student_pytop5()
# hw13_student()

#datetime 모듈
    #datetime: 날짜+시간 관리 클래스
    #date: 날짜만 관리 클래스
    #timedelta: 시간변화 관리 클래스

import datetime

def datetime_test1():
    now=datetime.datetime.now()
    print(now) #년도~초까지 속성(year,month,day,~,microsecond) 존재
    print(now.hour,now.minute)
    
    x_mas=datetime.date(2026,12,25)
    today=datetime.date.today()
    print(today)
    print(today.month,today.day)
    
    indep_day=datetime.date(2026,8,15)
    print(indep_day)
    print(indep_day-today) #date 객체끼리 뺄셈 가능, 자료형은 timedelta
    # indep_day<today도 가능
    rslt=indep_day-today
    print(f'올해 광복적까지 {rslt.days}일 남았습니다.')
# datetime_test1()

def date_list():
    from datetime import date
    lst=[date(2026,8,15),date(1919,3,1),date(2025,12,25)]
    print(lst)
    print(sorted(lst)) # 시간순으로 정렬됨
    print('제일 과거는?:',min(lst))
# date_list()

# 100일 후
def after100days():
    from datetime import datetime, timedelta
    #지금 이 시각 생성
    now=datetime.now()
    # print('100일 뒤:',now+100) # 정수는 못 더함
    print('100일 뒤:',now+timedelta(days=100))
    
    # lst=[100일 후, 10주 후, 3분 후]
    lst=[timedelta(days=100),timedelta(weeks=7),timedelta(minutes=3)]
    #timedelta 생성자에 들어가는 인자: weeks, days, hours, minutes, seconds, milliseconds, microseconds
    for x in sorted(lst):
        print(x)
        print(x.days)
        #timedelta의 속성: days, seconds, microseconds
# after100days()
    
def sleep_test():
    import time
    #엘레베이터 10층에서 3층까지 이동 경로 나타내기
    for x in range(10, 3-1, -1):
        print(x)
        time.sleep(0.5)
        
    for x in range(10, 3-1, -1):
        print(x,end=' ',flush=True)
        time.sleep(0.5)
    # !주의! 0.5초 간격으로 하나씩 출력 안됨;;
    # print 함수의 flush 인자를 True로
sleep_test()