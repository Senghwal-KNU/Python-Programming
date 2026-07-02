def hello():
    print('hello world!')
    print("-ㅇㅅㅁ")
    print('''여러줄
    출력''')
    #주석 단축키: ctrl+Q
    '''
    여러줄
    주석
    '''
#def로 코드 분리
def input_name():
    name=input('이름: ')
    print("안녕하세요,", name,'씨!')

#이름, 나이 입력받아, 10년 후 나이 출력하는 프로그램
#???씨 10년 후 ???세입니다.
def age_calculator():
    name=input("이름: ")
    age=input("나이: ")
    print(f"{name}씨 10년 후 {int(age)+10}세입니다.")
# year_calculator()

#직사각형
def rectagular():
    if True:
        x=float(input("직사각형의 가로: "))
        y=float(input("직사가형의 세로: "))
    else:
        raw=input("직사각형의 가로와 세로(공백으로 구분하여 입력하세요): ")
        x=float(raw.split()[0])
        y=float(raw.split()[1])
    print(f"둘레의 길이: {2*(x+y):.3f}")
    print(f"넓이: {x*y:.3f}")
    # diag=(float(x)**2+float(y)**2)**0.5
    # print("대각선의 길이:",diag)
rectagular()