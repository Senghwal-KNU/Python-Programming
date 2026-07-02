
def circleTest(): 
    radius = float(input('원의 반지름: '))
    print(f'반지름이 {radius}인 원의 넓이는 {radius*radius*3.14:.2f}, 둘레의 길이는 {radius*3.14*2:.2f}입니다.')
    
    
def arithmeticTest(): 
    a = int(input('정수 a: '))
    b = int(input('정수 b: '))
    
    #f-string 사용: 권장
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')