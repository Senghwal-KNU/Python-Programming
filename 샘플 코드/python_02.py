def rectangle_test(): 
    rslt = input('직사각형의 가로, 세로(공백으로 구분): ').split()
    garo, sero = [float(x) for x in rslt]
    lst = [float(x) for x in rslt]
    print('대각선의 길이:', (garo**2+sero**2)**.5)
    print('대각선의 길이:', (lst[0]**2+lst[1]**2)**.5)
    
def mail_test(): 
    mail = input('메일 주소: ')
    rslt = mail.split('@')
    print('ID:', rslt[0])
    print('Domain:', rslt[1])
    
def mail_test_v2(): 
    mail = input('메일 주소: ')
    _id, domain = mail.split('@')
    rslt = mail.split('@')

    print('ID:', _id)
    print('Domain:', domain)
    
def name_test(): 
    name = input('이름: ').split()
    print('중간 이름:', name[1])    
    
def name_test_v2(): 
    _, middle, _ = input('이름: ').split()
    #_: 익명 변수
    print('중간 이름:', middle)

def sum_test(): 
    l_side = input('식: ')
    lst = [float(x) for x in l_side.split('+')]
    print(f'{l_side} = {sum(lst):.1f}')
    
    
    
def list_test(): 
    print('0에서 9까지 숫자를 포함하는 리스트:', list(range(10)))
    print('0에서 9까지 숫자의 제곱 리스트:', [x**2 for x in range(10)])
    print('0에서 9까지 숫자 중 짝수 리스트:', list(range(0, 10, 2)))
    print('0에서 9까지 숫자 중 홀수의 제곱 리스트:', [y**2 for y in range(1, 10, 2)])
    lst = [-30,45,-5,-90,20,53,77,-36]
    rslt = [x for x in lst if x<0]
    print(rslt)
    
    ages = [34,39,20,18,13,54]
    rslt = [y for y in ages if y>=19]
    print(rslt)
      
def range_test(): 
    #0 이상 7 이하의 정수들 
    lst = list(range(8))
    print(lst)
    #5 이상 15이하의 정수들
    lst = list(range(5, 16))
    print(lst)
    #-3이상 3이하의 정수들
    lst = list(range(-3, 4))
    print(lst)
    #10미만의 양의 짝수들
    lst = list(range(2, 10, 2))
    print(lst)
    #10미만의 양의 홀수들
    lst = list(range(1, 10, 2))
    print(lst)
    #10미만의 양의 정수들 역순으로 
    lst = list(range(9, 0, -1))
    print(lst)
    #10이하의 양의 홀수들 역순으로 
    lst = list(range(9, 0, -2))
    print(lst)
    #20이상 50이하의 7의 배수들
    lst = list(range(21, 51, 7))
    print(lst)