def list순회1():
    lst2 = ['pancake.', 'kiwi juice.', 'espresso.']
    #c스타일
    for i in range(0,len(lst2)):
        print(f"c)I like {lst2[i]}")
    #py스타일
    for i in lst2:
        print(f"py)I like {i}")
# list순회1()

def list순회2():
    lst1 = ['I like', 'I love']
    lst2 = ['pancake.', 'kiwi juice.', 'espresso.']
    for i in lst1:
        for j in lst2:
            print(i,j)
# list순회2()

def list순회3():
    list1 = [3, 5, 7]
    list2 = [2, 3, 4, 5, 6]
    for i in list1:
        for j in list2:
            print(f"{i} * {j} = {i*j}")
# list순회3()

def list순회4():
    lst=[10,20,30,50,60]
    n,m=1,0
    for x in lst:
        n=n*x
        m+=x
    print("리스트의 원소들의 곱 :",n)
    print("리스트의 원소들의 합 :",m)
# list순회4()
        
def range순회1():
    print("1-1")
    print('1-2')
    print('1-3')
    for x in range(1,100+1):
        print(x, end=" ")
    print('\n1-4')
    for x in range(2,100+1,2):
        print(x, end=" ")
    print('\n1-5')
    for x in range(1,100+1,2):
        print(x, end=" ")
    print('\n1-6')
    for x in range(100,-1,-2):
        print(x, end=" ")
    print('\n1-7')
    for x in range(-100,0):
        print(x,end=" ")
# range순회1()

def range순회2():
    x=0
    for i in range(1,10+1):
        x+=i
        # print(x)
    print("1 이상 10 이하의 정수의 합:",x)
    x=0
    for i in range(2,100+1,2):
        x+=i
        # print(x)
    print("1 이상 100 이하의 짝수의 합:",x)
    x,y=0,1
    n=int(input("n: "))
    for i in range(1,n+1):
        x+=i
        y*=i
        # print(x)
    print(f"1이상 {n}이하의 정수의 합:",x)
    print(f"{n}!:",y)
# range순회2()

def range순회3():
    n=2
    for x in range(1,10):
        print(f"{n}X{x} = {n*x}")
# range순회3()

def range순회3_2():
    for a in range(2,10):
        for b in range(1,10):
            print(f"{a} X {b} = {a*b:2}",end="\t")
        print("")
# range순회3_2()

def range순회3_3():
    for a in range(1,10):
        for b in range(2,10):
            print(f"{b} X {a} = {a*b:2}",end="\t")
        print("")
# range순회3_3()

def while1():
    while True:
        player=input("가위, 바위, 보 중 하나를 선택하세요: ")
        if player in ['가위','바위','보']: #'가위 바위 보'.split() 도 가능
            print(f"{player}를 선택하셨습니다.")
            break
        else:
            print('[입력오류] 가위, 바위, 보 중 하나를 선택하세요.')
# while1()

def while2():
    while True:
        n=int(input("양의 정수: "))
        if n>0:
            print(f"1부터 {n}까지의 합: {(n*(n+1)//2)}")
            break
        else:
            print("[입력오류] 양의 정수를 입력해주세요.")
# while2()

def while3():
    nums=[]
    while True:
        usr=input("수: ")
        if (usr.strip()).lower() in ['quit']:
            #if len(usr)==0:
                #print('입력된 수 없음')
                #break
            print(f"4개 수들의 평균: {sum(nums)/len(nums)}")
            break
        else:
            nums.append(float(usr))
            print(nums)
# while3()

def 소수1():
    n=int(input("정수: "))
    for i in range(2,n):
        if n%i==0:
            print("소수가 아닙니다.")
            return()
    print("소수입니다.")
# 소수1()

def 소수2():
    #입력
    a=int(input("a: "))
    b=int(input("b: "))
    if a>b:
        a,b=b,a
    #판별
    lst=[]
    for i in range(a+1,b):
        flag=1 #1이면 소수
        for j in range(2,i):
            if i%j==0:
                flag=0
                break
        if flag==1:
            lst.append(i)
    #출력
    print(f"{a}와 {b} 사이의 소수:",*lst)
    print(f"{a}와 {b} 사이의 소수 개수: {len(lst)}")
# 소수2()

def 소수2_re():
    #입력
    a=int(input("a: "))
    b=int(input("b: "))
    if a>b:
        a,b=b,a
    #판별
    lst=[]
    for i in range(a+1,b):
        flag=1 #1이면 소수
        if len(lst)!=0:
            for n in range(0,len(lst)):
                if i%lst[n]==0:
                    flag=0
                    break
        if flag==1:
            for j in range(2,i):
                if i%j==0:
                    flag=0
                    break
        if flag==1:
            lst.append(i)
    #출력
    print(f"{a}와 {b} 사이의 소수:",*lst)
    print(f"{a}와 {b} 사이의 소수 개수: {len(lst)}")
소수2_re()