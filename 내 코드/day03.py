def 연산자1():
    n=int(input("정수: "))
    print(f"입력된 정수는 0에서 100 사이에 있는 짝수입니다: {n>0 and n<100 and n%2==0}")
    #0<n<100 and n%2==0, n in range(2,100,2)도 가능
# 연산자1()

def 연산자2():
    n=int(input("세 자리 정수를 입력하세요: "))
    print(n)
    one=n%10
    ten=n%100//10
    hun=n//100
    print(f"1의 자리: {one}")
    print(f"10의 자리: {ten}")
    print(f"100의 자리: {hun}")
    print("------")
    print(one,ten,hun,sep="")
# 연산자2()

def 조건문1():
    age=int(input("나이: "))
    if age<20:
        print("청소년 할인되었습니다.")
    print("입장하세요.")
# 조건문1()
    
def 조건문2():
    step=int(input("걸음 수: "))
    if step>=1000:
        print("목표 달성")
# 조건문2()

def 조건문3():
    hour=int(input("시간: "))
    if 0<=hour<12:
        print("오전입니다.")
    elif 12<=hour<=24:
        print("오후입니다.")
    else:
        print("시간오류.")
#hour not in range(24)도 가능
# 조건문3()

def 조건문4():
    spd=float(input("속도: "))
    if spd>=150:
        print("[입력오류] 속도는 0 이상 150 미만의 값만 가능합니다.")
    elif spd>=100:
        print("고속")
    elif spd>=60:
        print("중속")
    elif spd>=0:
        print("저속")
    else:
        print("[입력오류] 속도는 0 이상 150 미만의 값만 가능합니다.")
# 조건문4()

def 조건문5():
    score=int(input("점수: "))
    if score not in range(0,101):
        print("점수오류")
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    elif score>=60:
        print("D")
    else:
        print("F")
# 조건문5()

def 조건문6():
    age=int(input("나이를 입력하시오 : "))
    tall=int(input("키를 입력하시오(단위 cm) : "))
    if age>=19 and tall>=150:
        print("입장할 수 있습니다.")
    else:
        print("입장할 수 없습니다.")
# 조건문6()

def 조건문7():
    alp=input("알파벳을 입력하시오 :")
    mo='a,e,i,o,u'.split(",")
    # print(alp)
    # print(mo)
    if alp in mo:
        # if alp in 'aeiouAEIOU'도 가능
        print(alp, "(은)는 모음입니다.")
    else:
        print(alp, "(은)는 자음입니다.")
# 조건문7()

def 조건문8():
    y,m=[int(x) for x in input("년도, 월 (콤마로 구분하여 입력): ").split(",")]
    print(y,m)
    if not(0<m<13):
        print("[입력 오류]1월 ~ 12월만 존재합니다.")
        #return 사용 가능
    elif m==2:
        if (y%4==0 and y%100!=0) or y%400==0:
            print(f"{y}년 {m}월은 29일까지 존재합니다.")
        else:
            print(f"{y}년 {m}월은 28일까지 존재합니다.")
    elif m in (4,6,9,11):
        print(f"{y}년 {m}월은 30일까지 존재합니다.")
    else:
        print(f"{y}년 {m}월은 31일까지 존재합니다.")
# 조건문8()

def 조건문9():
    alp=input("문자: ")
    # print(alp.isalpha())
    #if alp.isalpha(): #한글도 포함
    if alp.isalpha() and alp.isascii():
        if alp in 'aeiouAEIOU':
            print(f"{alp}는 모음입니다.")
            rslt='모음'
        else:
            print(f"{alp}는 자음입니다.")
            rslt='자음'
    elif alp.isnumeric():
        print(f"{alp}는 숫자입니다.")
        rslt='숫자'
    else:
        print(f"{alp}는 기타문자입니다.")
        rslt='기타문자'
        
    print(f"{alp}는 {rslt}입니다.")
조건문9()