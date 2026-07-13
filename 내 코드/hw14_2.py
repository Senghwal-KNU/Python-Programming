def use_key():
    with open('words.txt','rt') as f:
        words=[word.rstrip() for word in f]
    
    print('words',words)
    
    print('파일의 내용 중 길이가 가장 긴 단어:',max(words,key=len))
    
    print('대소문자를 무시하고 사전식으로 정렬:',\
    ', '.join(sorted(words,key=lambda x:x.lower())))
    
    print('숫자가 가장 많이 포함된 단어:',\
    max(words, key=lambda word:len([n for n in word if n.isdigit()])))
    
    print('숫자의 합이 가장 큰 단어:',\
    max(words,key=lambda x:sum([int(n) for n in x if n.isdigit()])))
    
    top3=sorted(words,key=lambda x:x.count('0'),reverse=True)[:3]
    print('숫자 0이 가장 많이 포함된 단어 3개:',\
    ', '.join(top3))
use_key()

def use_datetime():
    import csv
    from datetime import datetime, date, timedelta
    
    # with open('bike_rent.csv','rt') as f:
        # parsed=csv.reader(f)
        # 기준_날짜_시간,집계_기준,시작_대여소_ID,시작_대여소_역,종료_대여소_ID,종료_대여소_역,전체_건수, 전체_이용_분 , 전체_이용_거리_m 
        # for _ in range(3):
            # next(parsed)
        
    def q1():
        with open('bike_rent.csv','rt') as f:
            parsed=csv.reader(f)
            #기준_날짜_시간,집계_기준,시작_대여소_ID,시작_대여소_역,종료_대여소_ID,종료_대여소_역,전체_건수, 전체_이용_분 , 전체_이용_거리_m 
            for _ in range(3):
                next(parsed)    
        
            data_lst=[]
            for data in parsed:
                rt_start=data[0]
                for x in '/-:':
                    rt_start=rt_start.replace(x,' ')
                lst=[int(x) for x in rt_start.split()[:3]]
                rt_start=date(*lst)
                data_lst.append(rt_start)
        print(f'총 {len(data_lst)}건의 내역이 기록되어 있습니다.')
        
        min_data=min(data_lst)
        max_data=max(data_lst)
        diff=max_data-min_data
        print(f'{min_data}~{max_data}까지 {diff.days}일간의 내역이 기록되어 있습니다.')
    # q1()
        
    def q2():
        with open('bike_rent.csv','rt') as f:
            parsed=csv.reader(f)
            for _ in range(3):
                next(parsed)
            
            data_lst=[]
            for data in parsed:
                rt_start=data[0]
                for x in '/-:':
                    rt_start=rt_start.replace(x,' ')
                lst=[int(x) for x in rt_start.split()]
                rt_start=datetime(*lst)
                data_lst.append(rt_start)
        dct={}
        for h in range(24):
            cnt=0
            for data in data_lst:
                if data.hour==h:
                    cnt+=1
            print(f'{h:2}시대:{cnt:>7}건')
            dct[h]=cnt
        # print(dct)
        min_h=min(dct,key=lambda x:dct[x])
        print(f'이용 건수가 가장 적은 시간대: {min_h}시({dct[min_h]}건)')
    # q2()
    
    def q3():
        with open('bike_rent.csv','rt') as f:
            parsed=csv.reader(f)
            for _ in range(3):
                next(parsed)
            
            data_lst=[]
            for data in parsed:
                start_station=data[3]
                end_station=data[5]
                
                start_data=data[0]
                for x in '/-:':
                    start_data=start_data.replace(x," ")
                start_lst=[int(x) for x in start_data.split()]
                start_time=datetime(*start_lst)
                
                usage_time=timedelta(minutes=float(data[-2]))
                
                lst=[start_station,end_station,start_time,usage_time]
                data_lst.append(lst)
            
        print('이용 시간이 가장 긴 내역 3건:')
        top3=(sorted(data_lst,key=lambda x:x[-1],reverse=True)[:3])
        for x in top3:
            print(f'{x[0]} ~ {x[1]} ({x[2]} 출발, 총 {(x[-1].seconds)/60}분 이용)')
            
        print()
        
        for x in top3:
            print(f'{x[0]} ~ {x[1]} ({x[2]} 출발, {x[2]+x[-1]} 도착, 총 {(x[-1].seconds)/60}분 이용)')
    # q3()
    
    def q4():
        with open('bike_rent.csv','rt') as f:
            parsed=csv.reader(f)
            for _ in range(3):
                next(parsed)
            
            st1=set()
            st2=set()
            
            data_lst=[]
            for data in parsed:
                start_station=data[3]
                end_station=data[5]
                st1.add(start_station)
                st2.add(end_station)
                data_lst.append(end_station)
        # print(st1)
        # print(st2)
        print('출발역에는 있으나 도착역에는 포함되지 않은 역:', ', '.join(st1-st2))
        # print(data_lst)
        
        
        dct={}
        for x in st2:
            dct[x]=data_lst.count(x)
        # print(dct)
        for x in sorted(dct):
            print(f'{x} - {dct[x]}건')
            
        for x in sorted(dct,key=lambda x:dct[x],reverse=True)[:5]:
            print(f'{x} - {dct[x]}건')
    # q4()
# use_datetime()