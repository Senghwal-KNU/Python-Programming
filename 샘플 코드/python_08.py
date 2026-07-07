def tuple_set1(): 
    st1 = input('문자열1: ').lower()
    st2 = input('문자열2: ').lower()    

    s1 = {x for x in st1 if x.isalpha()==True} 
    s2 = {x for x in st2 if x.isalpha()==True} 


    print('공통 알파벳:', ' '.join(s1 & s2))

    print('문자열1에만 출현한 알파벳(대소문자 무시):', ' '.join(s1.difference(s2)))

# tuple_set1()

def tuple_set3(): 
    msg = input('문자열: ').lower()
    s = {x for x in msg if x.isalpha()}
    print('출현한 알파벳:', ' '.join(s))

# tuple_set3()

def set1(): 
    s1 = {10, 20, 30, 40, 50, 60}
    s2 = {30, 40, 50, 60, 70, 80}

    print('어느 한 쪽에만 있는 원소:', s1 ^s2)
    print('첫 번째에만 있는 원소:', s1-s2)

# set1()
    

def q7_7(): 
    sales = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
    cnt = 0

    for i in range(len(sales)-1):
        if sales[i]>sales[i+1] : 
            cnt+=1

    print(f'지난 {len(sales)}일 동안 전일대비 매출이 감소한 날은 {cnt}일입니다.')

# q7_7()
def q7_8(): 
    tp = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)
    s = {x for x in tp if tp.count(x)>1}

    print('중복 원소는:', ', '.join(str(x) for x in s))


# q7_8()
def q7_9(): 
    tp = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
    s = tuple(set(tp))
    print('중복 제거 튜플:',s)

# q7_9()

def freq_elt(tp): 
    s = set(tp) #안해줘도 무방
    mode = tp[0] #우선 최빈값을 tp[0]로 둠 
    
    for x in s: 
        if tp.count(x)>tp.count(mode): 
            mode = x
        elif tp.count(mode)==tp.count(x): 
            if mode < x: 
                mode = x
    return mode

def q7_10(): 
    tp = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
    rslt = freq_elt(tp)
    print(f'{tp}에서 가장 많이 나타나는 원소: {rslt}')
    
    tp = (1, 2, 5, 4, 3, 2, 9, 4, 7, 8, 9, 9, 3, 7, 3)
    rslt = freq_elt(tp)
    print(f'{tp}에서 가장 많이 나타나는 원소: {rslt}')

# q7_10()


def q7_11(): 
    lst =  [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
    rslt = [x for x in lst if len(x) != 0]
    # rslt = [x for x in lst if x]
    
    print(f'빈 원소를 제거한 결과({len(rslt)}개): {rslt}')

# q7_11()



def q7_15(): 
    tp = (4, 5, 2, 3, 8, 1, 9, 0)
    
    for x in range(len(tp)): 
        print(tp[:len(tp)-x])
    
    
# q7_15()



def q7_17(): 
    a = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
    b = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)
    print(f'마을 A와 B에 보낼 투표용지의 개수는 각각 {sum(a[2:])} 장과 {sum(b[2:])} 장입니다.')
    
    
    print(f'마을 A와 B의 고령화 정도는 각각 {sum(a[7:])/sum(a):.3f}와 {sum(b[7:])/sum(b):.3f}입니다.')
    
    
# q7_17()



def q7_26(): 
    mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]
    
    usr = tuple(int(x) for x in input('두 정수:').split())
    
    if usr in mylist: 
        print(f'{mylist.index(usr)+1}번째에 {usr}원소가 있습니다.')
    elif usr[::-1] in mylist: 
        rvs = usr[::-1] 
        print(f'{usr} 원소는 없으나 {mylist.index(rvs)+1}번째에 {rvs} 원소가 있습니다')
    else: 
        print('이 원소는 없습니다. ')
    
# q7_26()