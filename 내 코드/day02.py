# lst=[1,2,-3,5,-2]
# rslt=[10*i for i in lst if i>0]
# print(rslt)

# scores=[80,73,100,92,45,23]
# rslt=[i for i in scores if i>=80]
# print(rslt) 

def list_test():
    lst=[2,4,6,8,10]
    print(lst)
    
    lst=list(range(2,11,2))
    print("even_list =",lst)
    
    nations=['Korea', 'China', 'India', 'Nepal']
    print("nations =",nations)
    
    friends=['길동','철수','은지','지은','영민']
    print("friends =",friends)
    
    xyz='XYZ'
    string=list(xyz)
    print("string =",string)
    
#list_test()

def q4():
    formula=input("덧셈식: ")
    numbers=formula.split("+")
    rslt=sum(float(x) for x in numbers)
    print(f"{formula} = {rslt:.1f}")
# q4()

def q1():
    raw=input("직사각형의 가로와 세로(공백으로 구분하여 입력하세요): ").split()
    x=float(raw[0])
    y=float(raw[1])
    print(f"대각선의 길이: {(x**2+y**2)**0.5}")
q1()