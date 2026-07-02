def after10years(): 
    name = input('이름: ')
    age = int(input('나이: '))
    print(f'{name}님의 10년 후 나이는 {age+10}세입니다.')
    
def rectangle_test(): 
    width = float(input('가로: '))
    height = float(input('세로: '))
    print(f'둘레의 길이는 {(width+height)*2}, 넓이는 {width*height}입니다. ')
    print('대각선의 길이:', (width**2+height**2)**.5)
    