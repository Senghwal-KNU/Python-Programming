def day_13_5():
    with open('weather.csv','rt') as f:
        import csv
        parsed=csv.reader(f)
        next(f) #
        lst=list(parsed)
    coldest_day=min(lst,key=lambda x:float(x[-2]))
    hottest_day=max(lst,key=lambda x:float(x[-1]))
    print('가장 추웠던 날: {} 기온 정보: 평균({}), 최저({}), 최고({})'\
    .format(coldest_day[0],coldest_day[2],coldest_day[3],coldest_day[4]))
    print('가장 더웠던 날: {} 기온 정보: 평균({}), 최저({}), 최고({})'\
    .format(hottest_day[0],hottest_day[2],hottest_day[3],hottest_day[4]))
# day_13_5()

def day_13_6():
    import csv
    n=10
    while True:
        try:
            f_name=input('파일 이름: ')
            with open(f_name,'rt') as f:    
                parsed=csv.reader(f)
                for _ in range(n-1):
                    next(parsed)
                print(f'{n}번째 라인:{','.join(next(parsed))}')
        except FileNotFoundError:
            print(f'{f_name} 파일을 찾을 수 없습니다. 파일 이름을 확인해주세요.')
        except StopIteration:
            print(f'{f_name} 파일에는 {n}번째 라인이 없습니다.')
day_13_6()