def mutable():
    dct1 = {'Monday':1, 'Tuesday':2}
    dct2 = {'Tuesday':2, 'Monday':1}

    def prnt():
        print('dct1:',dct1,'\ndct2:', dct2)
        print('dct1==dct2:', dct1 == dct2)
        print('id(dct1):',id(dct1),'\nid(dct2):',id(dct2))
        print('dct1 is dct2:', dct1 is dct2)
        print()
    
    prnt()
    
    dct1['Wednesday']=3
    
    prnt()
# mutable()

def immutable():
    x = 1
    y = 1
    print('x==y:', x==y)        
    print('x is y:', x is y)  
    print('id(x):',id(x),'\nid(y):',id(y))
    x*=10
    print('id(x):',id(x),'\nid(y):',id(y))
    y=10
    print('id(x):',id(x),'\nid(y):',id(y))
# immutable()

def mu_and_immu():
    def rrot(n,lst): # lst를 n만큼 오른쪽 로테이션
        for _ in range(n): # n%len(lst)번 반복하는 게 더 효율적
            lst.insert(0,lst.pop())
        return lst
    lst='dog cat tiger lion'.split()
    n=int(input('n: '))
    print(f'오른쪽으로 {n}칸 로테이션 후:',rrot(n,lst))
# mu_and_immu()

def mu_and_immu_re():
    def rrot(n,lst): # lst를 n만큼 오른쪽 로테이션
        for _ in range(n%len(lst)): # n%len(lst)번 반복하는 게 더 효율적
            lst.insert(0,lst.pop())
        # return lst 리스트 반환 안해도 매개변수로 받은 lst는 변경되어 있음
    lst='dog cat tiger lion'.split()
    n=int(input('n: '))
    rrot(n,lst)
    print(f'오른쪽으로 {n}칸 로테이션 후:',lst)
# mu_and_immu_re()

# 예외(Exception) 처리 => Goal: 에러 메시지 안뜨게
# 정수 입력 받아 10만큼 큰 수 출력
def plus10():
    while True:
        try: # 예외 가능성 있는 문장 모두 넣기
            n=int(input('n: '))
            m=int(input('m: '))
            
            print(f'{n}+10 = {n+10}')
            print(f'{n}/{m} = {n/m}')
            
            break
               
        # except ValueError:
            # print('잘못된 값 입력됨')
        # except ZeroDivisionError:
            # print('m에 0 입력됨')
        
        # except: # 모든 예외 처리(사용 미권장), 예외 처리 중에서 제일 끝에 써야함
            # print('예외 발생')
        except Exception as e: # 모든 예외 처리
            print('예외 발생', {type(e).__name__})
# plus10()

def write_test(): # 주로 쓰는 형태는 아님
    # 'my_info.txt'에 내 이름, 나이, 소속 쓰기
    # 1. 파일에 스트림 연결: 파일 객체 생성
    # open('파일이름', '모드 및 파일형식') 모드: 읽기(r), 쓰기(w) 등, 파일형식: 텍스트(t), 바이너리(b) 등
    f=open('my_info.txt','wt')
    # 2. 쓰기
    print('이름: 홍길동', file=f)
    print('나이: 5세', file=f)
    # 3. 스트림 해제
    f.close()
# write_test()

def write_test_final():
    # 파일 자동으로 닫기
    with open('my_info.txt','wt') as f:
        print('이름: 둘리',file=f)
        print('나이: 1세',file=f)
        f.write('소속: 지구\n') # write(): 문자만 받음, 개행x
        #with 블록이 끝나면 자동으로 f.close() 실행됨
    print('파일 쓰기 완료')
# write_test_final()

def read_test():
    try:
        with open('my_info.txt','rt') as f:
        #상대경로(소스파일이 소속된 폴더를 기준으로함), 절대경로
            print('print(next(f))로 읽기')
            #try: 여기 말고 with 블럭 전체 감싸기
            print(next(f).rstrip())# 한 줄 끝에 있는 개행 지우기
            print(next(f).rstrip())
            print(next(f),end="")
            print(next(f),end="") # 오류(StopIteration) 발생
    except StopIteration:
        print('파일 다 읽음')
    except FileNotFoundError:
        print('파일 없음')
        
    print() 
       
    try:
        with open('my_info.txt','rt') as f:
            print('for문으로 읽기')
            for x in f:
                print(x.rstrip())
    except StopIteration:
        print('파일 다 읽음')
    except FileNotFoundError:
        print('파일 없음')    
# read_test()

# print(f.read()) 파일 내용 모두 읽기
# print(f.read(2)) 파일에서 1글자 읽어옴
# print(f.raedline()) 한 줄 읽기
# print(f.readlines())

def file_1():
    with open('we_will_rock.txt','rt') as f:
        for x in f:
            print(x.rstrip())
# file_1()

def file_2():
    f_name=input('파일의 이름 : ')
    tmp=''
    try:
        with open(f_name,'rt') as f:
            for x in f:
                tmp+=x.upper()
        
        with open(f_name[:-4]+'_upper.txt','wt') as f:
            print(tmp,file=f)
    except FileNotFoundError:
        print(f_name, '파일이 없습니다.')
# file_2()

def file_3():
    try:
        with open('sales.txt','rt') as f:
            lst=[int(x) for x in f]
    except FileNotFoundError:
        print('sales.txt 파일이 없습니다.')
    with open('summary.txt','wt') as f:
        f.write(f'총매출 = {sum(lst)}\n')
        f.write(f'평균 일매출 = {sum(lst)/len(lst)}')
# file_3()    

def file_4():
    try:
        with open('fruits.txt','rt') as f:
            lst=[x.rstrip().lower() for x in f]
            print(lst)
    except FileNotFoundError:
        print('fruits.txt 파일이 없습니다.')
    
    import string
    dct={x:0 for x in string.ascii_lowercase}
    # print(dct.get('a',1))
    for x in lst:
        for y in x:
            dct[y]=dct.get(y,0)+1
    print(dct)
# file_4()

def csv_test():
    with open('weather.csv','rt') as f:
        n=9
        for _ in range(n):
            next(f)
        tmp=next(f)
    lst=tmp.split(',') # [날짜, 평균, 최저, 최고]
    print(lst[-1])

    with open('weather.csv','rt') as f:
        n=6
        for _ in range(n):
            next(f)
        tmp=next(f)
    lst=tmp.split(',') # [날짜, 평균, 최저, 최고] 근데 내용에 쉼표가 있으면..?
    print(lst[1])
# csv_test()
    
# csv 모듈 사용
def csv_test2():
    import csv
    with open('weather.csv','rt') as f:
        parsed=csv.reader(f)
        # 이제부터 f는 parsed로도 접근가능
        print(next(parsed)) # 리스트 형태로 출력됨
        print(next(f)) # 문자열 형태로 출력됨
# csv_test2()

def coldest_day():
    # 가장 추웠던 날 찾기: 최저기온이 가장 낮은 날짜와 그 날짜의 최저 기온
    import csv
    with open('weather.csv','rt') as f:
        parsed=csv.reader(f)
        coldest_temp=100
        
        next(parsed) # 헤더(날짜, 지점, 평균기온..) 날리기
        
        for x in parsed:
            if float(x[-2])<coldest_temp:
                coldest_temp=float(x[-2])
                coldest_day=x[0]
    print(f'가장 추웠던 날: {coldest_day}, 최저기온: {coldest_temp}')
# coldest_day()
    
def coldest_day2():
    import csv
    with open('weather.csv','rt') as f:
        parsed=csv.reader(f)
        next(parsed)
        
        lst=[float(x[-2]) for x in parsed]
        
    print(f'가장 추웠던 날:  (최저기온: {min(lst)})')
# coldest_day2()
    
def key_test():
    lst='Z bc defffff Sss xssss yddd'.split()
    print(lst)
    print(sorted(lst))
    print(sorted(lst,key=str.lower)) # 대소문자 무시한 사전식 정렬, lower뒤에 ()안쓰는 거에 유의
# key_test()
    
def file_5():
    import csv
    with open('weather.csv','rt') as f:
        parsed=csv.reader(f)
        tmp=list(next(parsed))
        lst1=tmp
        lst2=tmp
        for x in parsed:    
            # if x[-2]<lst1[-2]:
                # lst1=list
            # if x[-1]>lst2[-1]:
                # lst2=list        
    print(lst1)
    print(lst2)
                
        
    print('가장 추웠던 날: {} 기온 정보: 평균({}), 최저({}), 최고({})'.format())
    print('가장 더웠던 날: {} 기온 정보: 평균({}), 최저({}), 최고({})'.format())
file_5()