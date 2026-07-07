# sequence: 인덱싱, 슬라이싱 가능 자료형- list, tuple, str, range
# iterable: 반복가능객체, for문 뒤에 작성 가능- sequence, set, dict

def use_list():
    basket='사과,바나나,사과,포도,바나나,사과'.split(",")
    cnt[3,2,1]

    frt=input('과일: ').strip()
    if frt=='사과':
        x=cnt[0]
    elif frt=='바나나':
        x=cnt[1]
    elif frt=='포도':
        x=cnt[2]
    print(f'{frt}의 개수는 {x}')

def use_dict():
    dct={'사과':3,'바나나':2,'포도':1}
    #dict={key:value}
    
    str_fruits='사과 바나나 포도'
    lst_cnt=[3,2,1]
    dct={str_fruits.split()[i]:lst_cnt[i] for i in range(len(lst_cnt))}
    print(dct)
# use_dict()
    
def p7_3():
    menu={
    'Americano':3000,
    'Ice Americano':3500,
    'Cappuccio':4000,
    'Cafe Latte':4500,
    'Espresso':3600
    }
    for x in menu:
        print(f'{x}\t가격 : {menu[x]:,}원')
    order=input('위의 메뉴중 하나를 선택하세요: ')   
    if order in menu:
        print(f'{order}는 {menu[order]:,}원 입니다. 결제를 부탁합니다.')
    else:
        print(f'미안합니다. {order}는 메뉴에 없습니다.')
# p7_3()

def dict_test1():
    # 딕셔너리 생성 1: 원소 나열
    dct={'뽀로로':1,'크롱':2}
    # key는 immutable한 것만 가능- str, tuple, int, float
    # mutable: list, set, dict
    
    # 딕셔너리 생성 2: 캐스팅(어려움)
    # 하나의 성분이 2개의 자료로 구성된 경우에만 가능
    lst=[['야호',1],('호야',2)]
    dct=dict(lst) # 가능 {'야호':1, '호야':2}
    
    # 딕셔너리 생성 3: 딕셔너리 축약
    str_menu='Americano, Ice Americano, Cappuccio, Cafe Latte, Espresso'
    lst_menu=str_menu.split(', ')
    str_price='3,000원, 3,500원, 4,000원, 4,500원, 3,600원'
    lst_price=[int(x) for x in str_price.replace(',','').replace('원','').split()]
    
    dct={1,2,3} # set
    dct={} # dict
    
    dct_menu={lst_menu[i]:lst_price[i] for i in range(len(lst_menu))}
    print(dct_menu)
    
    # 딕셔너리 출력
    for i in dct_menu:
        print(f'{i}: {dct_menu[i]}')
    
    for k,v in dct_menu.items():
        print(f'{k}: {v}')
        
    # 원소 추가
    dct_menu['빙수']=10000
    print(dct_menu)
    
    # 원소 제거
    del dct_menu['빙수']
    print(dct_menu)
    
    print(dct_menu.pop('Espresso')) # dict.pop(인자 꼭 넣어야함), 제일 끝 성분 뽑으려면 dict.popitem()
    print(dct_menu)
    
    print(dct_menu.popitem())
    print(dct_menu)
    
    print('카푸치노 가격:',dct_menu.get('Cappuccio',0)) # dict.get(키,Default=None)
# dict_test1()

def p7_1():
    price = {'김밥 ': 5000, '어묵 ': 3000, '떡볶이 ': 2000}
    print('(1)',price['김밥 '])
    
    price['김밥 ']=6000
    print('(2)',price)
    
    print('(3)',price.values())
    
    print('(4)',price.keys())
    
    print('(5)',f'이 식당의 메뉴 개수는 {len(price)}개 입니다.')
# p7_1()

def dict1():
    dct={x:x**2 for x in range(1,11)}
    print(dct)
# dict1()

def dict2():
    dct={'옷':100_000,'컴퓨터':2_000_000,'모니터':320_000} # 밑줄(_)은 자릿수 구분할 뿐 100_000은 int
    # print(dct.values())
    price=[int(dct[x]) for x in dct]
    print(f'합계: {sum(price):,}원')
# dict2()

def dict3():
    colors = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    c_dct={colors[i]:values[i] for i in range(len(colors))}
    print('c_dct =',c_dct)
# dict3()

def dict3_zip():
    pass
# dict3_zip()

def dict4():
    lst_month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    dct_month={i+1:lst_month[i] for i in range(len(lst_month))}
    print(dct_month)
    
    n=int(input('달: '))
    print(dct_month.get(n,'해당 달은 존재하지 않습니다.'))
# dict4()

def dict4_zip():
    lst_month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    dct_month=dict(zip(range(1,12+1),lst_month))
    # print(dct_month)
    
    n=int(input('달: '))
    print(dct_month.get(n,'해당 달은 존재하지 않습니다.'))
dict4_zip()

def dict5():
    score = {'Kim': [99,83,95], 'Lee': [68,45,78], 'Choi':[25,56,69]}
    for x in score:
        print(f'{x}\t: {sum(score[x])/len(score[x]):.3f}점')
# dict5()

def dict6():
    name='Kim Lee Choi'.split()
    score={}
    for x in name:
        x_score=[int(x) for x in input(f'{x}의 성적을 입력해주세요(성적은 공백으로 구분): ').split()]
        score[x]=x_score
        # print(score)
    
    for x in score:
        print(f'{x} : {score[x]}')
# dict6()

def p7_16():
    student_tuple = (('191101', '홍길동', '010-123-45xx'), ('191102', '임꺽정', '010-223-45xx'), ('191103', '장길산', '010-323-45xx') )
    
    student_dct = {student_tuple[i][0]:student_tuple[i][1] for i in range(len(student_tuple))}
    print('학생 정보:',student_dct)
    
    while True:
        student_id=input('학번을 입력하세요 : ').strip()
        if int(student_id)>=0:
            if student_dct.get(student_id):
                print(f'{student_id}번 학생은 {student_dct.get(student_id)}입니다.')
            else:
                print('해당 학번의 학생이 없습니다.')
        else:
            print('프로그램을 종료합니다.')
            break
# p7_16()

def p7_20():
    scores = ( ('박동규', 88, 95, 90), ('강영민', 85, 90, 95), ('박동민', 70, 90, 80), ('홍승주', 90, 90, 95))
    
    k_sum,m_sum,s_sum=0,0,0
    
    for x in scores:
        k_sum+=x[1]
        m_sum+=x[2]
        s_sum+=x[3]
        
    print('학생들의 수학 성적의 평균은 {}입니다.'.format(m_sum/len(scores)))
    print('학생들의 수학과 과학 성적의 평균은 {}입니다.'.format((m_sum+s_sum)/(len(scores)*2)))
    
    student_dic={x[0]:(sum(x[1:])/len(x[1:])) for x in scores}
    print('이름\t평균성적\n---------------------')
    for x in student_dic:
        print(f'{x}\t{student_dic[x]:.2f}')
# p7_20()