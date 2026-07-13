def Farm_class():
    class Farm:
        def __init__(self,name,typ,address,population):
            self._name=name
            self._type=typ
            self._address=address
            self._population=population
        
        def __repr__(self):
            return f'{self._name}: {self._address} ({self._type}, {self._population})'
   
        def get_population(self):
            return self._population
            
        def get_name(self):
            return self._name
            
        def get_type(self):
            return self._type
   
    def test_code_2():
        farm1 = Farm('대평한우목장','한우','경상남도 진주시 대평면 신풍길 143-8',25)
        #경상남도 진주시 대평면 신풍길 143-8에서 한우 25 마리를 사육하는 대평한우목장을 생성
        print(farm1)
    # test_code_2()
    
    import csv
    with open('farm.csv','rt') as f:
        parsed=csv.reader(f) 
        next(parsed)
        farm_list=[Farm(x[0],x[1],x[2],int(x[3])) for x in parsed]

    def test_code_3():
        print(farm_list)
    # test_code_3()

    def test_code_4():
        rslt=sorted(farm_list,key=Farm.get_population,reverse=True)[:5]
        for x in rslt:
            print(x)
    # test_code_4()
    
    def test_code_5():
        rslt=sorted(farm_list,key=Farm.get_name)[:3]
        for x in rslt:
            print(x)
    # test_code_5()
    
    st={x.get_type() for x in farm_list}
    
    def test_code_6():
        print('가축 타입:',', '.join(st))
    # test_code_6()
    
    def test_code_7():
        print('가축 타입과 농장 수')
        for x in st:
            cnt=0
            for y in farm_list:
                if x==y.get_type():
                    cnt+=1
            print(f'{x}: {cnt} 개의 농장')
    # test_code_7()

    def test_code_8():
        inp=input('가축 타입: ')
        if inp in st:
            cnt=0
            for x in farm_list:
                if x.get_type()==inp:
                    cnt+=x.get_population()
            print(f'{inp}(은)는 {cnt} 마리 사육 중 입니다.')
        else:
            print(f'{inp} 사육 농장은 없습니다.')
    # test_code_8()
# Farm_class()

def datatime_module():
    import datetime
    
    def q1():
        y,m,d=[int(x) for x in input('년도 월 일(공백으로 구분): ').split()]
        inp=datetime.date(y,m,d)
        today=datetime.date.today()
        print(f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다.',end=' ')
        if inp<today:
            print(f'{inp.year}년 {inp.month}월 {inp.day}일은 {(today-inp).days}일 전입니다.')
        elif inp>today:
            print(f'{inp.year}년 {inp.month}월 {inp.day}일은 {(inp-today).days}일 후입니다.')
        elif inp==today:
            print(f'{inp.year}년 {inp.month}월 {inp.day}일은 오늘입니다.')
    # q1()
    
    def q1_1():
        y,m,d=[int(x) for x in input('년도 월 일(공백으로 구분): ').split()]
        inp=datetime.date(y,m,d)
        today=datetime.date.today()
        dct=dict(zip(range(7),'월화수목금토일'))
        print(f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다.',end=' ')
        if inp<today:
            print(f'{inp.year}년 {inp.month}월 {inp.day}일({dct[inp.weekday()]})은 {(today-inp).days}일 전입니다.')
        elif inp>today:
            print(f'{inp.year}년 {inp.month}월 {inp.day}일({dct[inp.weekday()]})은 {(inp-today).days}일 후입니다.')
        elif inp==today:
            print(f'{inp.year}년 {inp.month}월 {inp.day}일({dct[inp.weekday()]})은 오늘입니다.')
    # q1_1()
    
    def q1_2():
        while True:
            try:
                y,m,d=[int(x) for x in input('년도 월 일(공백으로 구분): ').split()]
                inp=datetime.date(y,m,d)
                today=datetime.date.today()
                dct=dict(zip(range(7),'월화수목금토일'))
                print(f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다.',end=' ')
                if inp<today:
                    print(f'{inp.year}년 {inp.month}월 {inp.day}일로부터 {(today-inp).days}일 지났습니다.')
                elif inp>today:
                    print(f'{inp.year}년 {inp.month}월 {inp.day}일({dct[inp.weekday()]})은 {(inp-today).days}일 후입니다.')
                elif inp==today:
                    print(f'{inp.year}년 {inp.month}월 {inp.day}일({dct[inp.weekday()]})은 오늘입니다.')
                break
            except ValueError:
                print('[입력 오류] 입력하신 날은 존재하지 않습니다. 다시 입력해주세요.')
    # q1_2()
    
    def q2():
        m,d=[int(x) for x in input('생일을 입력해주세요(월과 일을 공백으로 구분): ').split()]
        b_day=datetime.date(datetime.date.today().year,m,d)
        today=datetime.date.today()
        if b_day==today:
            print('생일 축하합니다!')
        elif b_day>today:
            print('올해 생일까지 {}일 남았습니다.'.format((b_day-today).days))
        elif b_day<today:
            b_day=b_day+datetime.timedelta(days=365)
            print('올해 생일은 이미 지났네요. 내년 생일까지 {}일 남았습니다.'.format((b_day-today).days))
    q2()
datatime_module()