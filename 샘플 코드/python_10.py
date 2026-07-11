def q7_3(): 
    str_menu = 'Americano, Ice Americano, Cappuccino, Caffe Latte, Espresso'
    menu_lst = str_menu.split(', ')

    str_price = '3,000원, 3,500원, 4,000원, 4,500원, 3,600원'.replace(',', '').replace('원', '').split()
    price_lst =[int(x) for x in str_price]

    dct = dict(zip(menu_lst, price_lst))
    
    for x in dct: 
        print(f'{x}\t 가격: {dct[x]:,}원')
        
    usr = input('위의 메뉴중 하나를 선택하세요: ')   
    usr_title = usr.title()
    if usr_title in dct: 
        print(f'{usr}는 {dct[usr_title]:,}원 입니다. 결제를 부탁합니다.')
    else: 
        print(f'미안합니다. {usr}는 메뉴에 없습니다.')
# q7_3()

def dict1(): 
    dct = {x:x**2 for x in range(1, 11)}
    print(dct)
# dict1()
    
def dict2(): 
    dct = {'옷': 100_000, '컴퓨터': 2_000_000, '모니터': 320_000}
    print(f'합계: {sum(dct.values()):,}원')
# dict2()
        
def dict3(): 
    colors = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    
    #1 dictionary comprehension
    dct = {colors[i]:values[i] for i in range(len(colors))}
    print(dct)

    #2 zip()
    dct = dict(zip(colors, values))
    print(dct)
# dict3()
    
def dict4(): 
    eng_month = 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
    
    dct = dict(zip(range(1, 13), eng_month))
    
    month = int(input('달: '))
    
    print(dct.get(month, '해당 달은 존재하지 않습니다.'))    
# dict4()

def dict5(): 
    score = {'Kim': [99,83,95], 'Lee': [68,45,78], 'Choi':[25,56,69]}
    
    for x in score: 
        print(f'{x:5s}: {sum(score[x])/len(score[x]):.2f}점')    
# dict5()

def dict6(): 
    names = 'Kim Lee Choi'.split()
    score = {}
    for x in names: 
        score[x] = [int(n) for n in input(f'{x}의 성적을 입력해주세요: ').split()]
        
    
    for x in score: 
        print(f'{x:5s}: {score[x]}')   
# dict6()


def q7_16(): 
    student_tuple = (('191101', '홍길동', '010-123-45xx'), ('191102', '임꺽정', '010-223-45xx'), ('191103', '장길산', '010-323-45xx') )
    dct = {x[0]:x[1] for x in student_tuple}
    print('학생 정보:', dct)
    
    while True: 
        std_id = input('학번: ').strip()
        if std_id == '-1': 
            print('프로그램을 종료합니다. ')
            break
        
        if std_id in dct: 
            print(f'{std_id}번 학생은 {dct[std_id]}입니다.')
        else: 
            print('해당 학번의 학생이 없습니다.')
# q7_16()


def q7_20(): 
    scores = (('박동규', 88, 95, 90), ('강영민', 85, 90, 95), ('박동민', 70, 90, 80), ('홍승주', 90, 90, 95))
    math = [x[2] for x in scores]
    print('수학 평균:', sum(math)/len(math))

    science = [x[-1] for x in scores]
    print('수학, 과학 평균:', sum(math+science)/len(math+science))
    print()
    dct = {x[0]:x[1:] for x in scores}
    print('이름\t평균성적')
    print('-'*15)
    for x in dct: 
        print(f'{x}\t{sum(dct[x])/len(dct[x]):.2f}점') 
        
# q7_20()