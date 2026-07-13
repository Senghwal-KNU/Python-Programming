def genOTP():
    import random
    
    otp=random.randint(0,999999)
    print(otp)
    
def people():
    person1 = ['온달', 20, 1, 180.0, 100.0]
    person2 = ['이사부', 25, 1, 170.0, 70.0]
    person3 = ['평강', 22, 0, 169.0, 60.0]
    person4 = ['혁거세', 40, 1, 150.0, 50.0]
    #인당 5개
    #이름, 나이, 성별, 키, 몸
    
    person_list=person1+person2+person3+person4
    
    def how_many_persons(person_list):
        n=len(person_list)/5
        return n
    
    n_persons=how_many_persons(person_list)
# people()

def file1():
    with open('we_will_rock.txt','rt') as f:
        for x in f:
            print(x.rstrip())
# file1()

def file2():
    f_name=input('파일의 이름 : ')
    upper_name=f_name[:-4]+'_upper2.txt'
    
    lst_upper=[]
    with open(f_name,'rt') as f:
        for ln in f:
            ln_upper=ln.rstrip().upper()
            print(ln_upper)
            lst_upper.append(ln_upper)
    
    with open(upper_name,'wt') as f:
        for ln in lst_upper:
            print(ln,file=f)
# file2()

def file3():
    with open('sales.txt','rt') as f:
        lst=[int(n) for n in f]
        print('총매출 =',sum(lst))
        print('평균 일매출 =',sum(lst)/len(lst))
# file3()

def file4():
    import string
    
    with open('fruits.txt','rt') as f:
        lst=[x.rstrip() for x in f]
        
    dct={}
    for x in string.ascii_lowercase:
        cnt=0
        for word in lst:
            cnt+=word.lower().count(x)
        dct[x]=cnt
    print(dct)
# file4()

def file5():
    import csv
    
    with open('weather.csv','rt') as f:
        parsed=csv.reader(f)
        next(parsed)
        
        data_lst=[]
        for x in parsed:
            lst=[x[0],float(x[-3]),float(x[-2]),float(x[-1])]
            data_lst.append(lst)
        
        coldest_day=min(data_lst,key=lambda lst:lst[-2])
        hottest_day=max(data_lst,key=lambda lst:lst[-1])
        print('가장 추웠던 날: {} 기온 정보: 평균({}), 최저({}), 최고({})'.format(*coldest_day))
        print('가장 더웠던 날: {} 기온 정보: 평균({}), 최저({}), 최고({})'.format(*hottest_day))
# file5()

def file6():
    while True:
        f_name=input('파일명: ').strip()
        try:
            with open(f_name,'rt') as f:
                for _ in range(9):
                    next(f)
                print('10번쨰 라인:'+next(f).rstrip())
                break
        except FileNotFoundError:
            print(f'{f_name} 파일을 찾을 수 없습니다. 파일 이름을 확인해주세요.')
        except StopIteration:
            print(f'{f_name} 파일에는 10번째 라인이 없습니다.')
file6()