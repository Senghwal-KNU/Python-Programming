def scores_1():
    import csv
    with open('scores.csv','rt') as f:
        parsed=csv.reader(f)
        next(parsed)
        next(parsed)
        
        dct={x[0]:tuple(int(n) for n in x[1:]) for x in parsed}
        f_name=(f.name[:-4]+'_dct.txt')
    with open(f_name,'wt') as f:
        for x in dct:
            print(f'{x}: {dct[x]}',file=f)
        print(f'폴더 내 {f_name} 파일을 확인해주세요.')
# scores_1()

def scores_2():
    import csv
    with open('scores.csv','rt') as f:
        parsed=csv.reader(f)
        next(parsed)
        next(parsed)
        
        dct={x[0]:tuple(int(n) for n in x[1:]) for x in parsed}        
    
    name=input('이름: ')
    if name in dct:
        print(f'{name} 학생의 성적은 {dct[name]} 입니다.')
    else:
        print(f'{name} 학생은 존재하지 않습니다.')
# scores_2()
    
def scores_2_2():
    import csv
    with open('scores.csv','rt') as f:
        parsed=csv.reader(f)
        next(parsed)
        next(parsed)
        
        dct={x[0]:tuple(int(n) for n in x[1:]) for x in parsed}
    
    while True:
        n=input('총점: ')
        if n.isdigit():
            n=int(n)
            break
        else:
            print('[입력오류] 점수는 정수로 입력해주세요.')
    
    lst=[x for x in dct if sum(dct[x])==n]
    if lst:
        print(f'총점이 {n}인 학생: {', '.join(lst)}')
    else:
        print(f'총점이 {n}인 학생은 존재하지 않습니다.')
# scores_2_2()

def scores_3():
    import csv
    with open('scores.csv','rt') as f:
        parsed=csv.reader(f)
        next(parsed)
        next(parsed)
        
        dct={x[0]:tuple(int(n) for n in x[1:]) for x in parsed}
      
    py=tuple(dct[x][1] for x in dct)
    print(f'파이썬 성적: {py}')
# scores_3()

def Student():
    class Student:
        def __init__(self,name,py,cpp):
            self.__name=name
            self.__py=py
            self.__cpp=cpp
        
        def __str__(self):
            return f'파이썬 {self.__py}점, C++ {self.__cpp}점인 {self.__name} 학생입니다.'
            
        def __repr__(self):
            return f'<{self.__name} - 파이썬: {self.__py}점, C++: {self.__cpp}점>'
    
        def get_name(self):
            return self.__name
            
        def sum_score(self):
            return self.__py+self.__cpp
            
        def __ge__(self,other):
            return self.sum_score()>=other.sum_score()
            
        def __lt__(self,other):
            return self.sum_score()<other.sum_score()
    
    def test_code_1():
        pororo = Student('뽀로로', 10, 10)
        print(pororo)
    # test_code_1()

    import csv
    lst=[]
    with open('scores.csv','rt') as f:
        parsed=csv.reader(f)
        next(parsed)
        next(parsed)
        for x in parsed:
            name,_,py,_,cpp=x
            lst.append(Student(name,int(py),int(cpp)))
            
    def test_code_2():
        print(lst)
    # test_code_2()
    
    def test_code_2_2():
        print(f'{lst[0].get_name()}의 총점 >= {lst[1].get_name()}의 총점:', lst[0]>=lst[1]) #중괄호 안 빈 곳을 적절히 완성할 것.
        print('총점 순 내림차순 정렬:', sorted(lst, reverse = True))
        highest = max(lst)
        print(f'최고득점자: {highest.get_name()}(총점 {highest.sum_score()}점)') #중괄호 안 빈 곳을 적절히 완성할 것.
    # test_code_2_2()
# Student()

def dict_comp_1():
    fruits = {'Apple': '사과', 'Strawberry': '딸기', 'Peach': '복숭아', 'Grape': '포도'}
    lst=[x+'='+fruits[x] for x in fruits]
    print(lst)
# dict_comp_1()

def dict_comp_2():
    fruits_list = ['Apple=사과', 'Strawberry=딸기', 'Peach=복숭아', 'Grape=포도']
    fruits={x.split('=')[0]:x.split('=')[1] for x in fruits_list}
    print(fruits)
dict_comp_2()