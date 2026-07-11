import csv
def score_test1(): 
    with open('scores.csv', 'rt') as f: 
        parsed = csv.reader(f)
        next(parsed)#헤더 제거 
        next(parsed)
        
        # dct 생성 1 : 파일 한 라인씩 읽어 처리 
        dct = {}
        for x in parsed: 
            #x[0]가 이름, key
            #x[1:]가 점수, value -> 성분을 모두 숫자로 바꿔야 함. 
            
            #성분 모두 숫자로 변경
            tp = tuple(int(n) for n in x[1:]) 
            #딕셔너리에 추가 
            dct[x[0]] = tp 
            
        # dct 생성 2 : 딕셔너리 축약
        # dct = {x[0]:tuple(int(n) for n in x[1:]) for x in parsed}
        # 오히려 가독성이 떨어짐 -> 이런 경우 축약은 권장되지 않음.
    with open('score_dct.txt', 'wt') as f: 
        for x in dct: 
            print(f'{x}: {dct[x]}', file = f)
    print(f'폴더 내 {f.name} 파일을 확인해주세요.') #파일 객체에 name 속성은 파일명을 의미
    #파이썬에서 변수의 영역은 블록이 아니라 함수이므로 with 블록이 끝난 시점에도 f의 속성에는 접근 가능. 이미 파일이 닫혔기 때문에, 읽기/쓰기 등의 메소드는 사용 불가. 
# score_test1() 
        
def score_test2(): 
    with open('scores.csv', 'rt') as f: 
        parsed = csv.reader(f)
        next(parsed)#헤더 제거  
        next(parsed)
        dct = {}
        for x in parsed: 
            tp = tuple(int(n) for n in x[1:]) 
            dct[x[0]] = tp 
            
    name = input('이름: ').strip()
    if name in dct: 
        print(f'{name} 학생의 성적은 {dct[name]} 입니다.')
    else: 
        print(f'{name} 학생은 존재하지 않습니다.')

# score_test2() 
 
 
def score_test3(): 
    while True: 
        try: 
            with open('scores.csv', 'rt') as f: 
                parsed = csv.reader(f)
                next(parsed)#헤더 제거  
                next(parsed)
                dct = {}
                for x in parsed: 
                    tp = tuple(int(n) for n in x[1:]) 
                    dct[x[0]] = tp 
             
            score = int(input('총점: '))
            break
        except ValueError: 
            print('[입력오류] 점수는 정수로 입력해주세요.')
        
    #아래 문장은 예외발생할 여지가 없기에 try문에서 빼도 됨. 
    rslt = [x for x in dct if sum(dct[x]) == score] #이 정도의 축약은 가독성 좋음: 권장!

    if rslt: 
        print(f'총점이 {score}인 학생:', ', '.join(rslt))
    else: 
        print(f'총점이 {score}인 학생은 존재하지 않습니다.')

    
# score_test3() 
 
 
def score_test4(): 
    with open('scores.csv', 'rt') as f: 
        parsed = csv.reader(f)
        next(parsed)#헤더 제거  
        next(parsed)
        dct = {}
        for x in parsed: 
            tp = tuple(int(n) for n in x[1:]) 
            dct[x[0]] = tp 
         
    python = tuple(x[1] for x in dct.values())
    print('파이썬 성적:', python)

        
    # (선택) unzip 풀이: zip(*)
    # 아래 풀이는 심화입니다. 원하는 분만 확인해주세요. 
    # _, python, _, _  = zip(*dct.values())
    # print('파이썬 성적:', python)
    
# score_test4() 



class Student: 
    def __init__(self, name, py, cpp): 
        self._name = name
        self._py = py
        self._cpp = cpp
    
    def __str__(self): 
        return f'파이썬 {self._py}점, C++ {self._cpp}점인 {self._name} 학생입니다. '
        
    def __repr__(self): 
        return f'<{self._name} - 파이썬: {self._py}점, C++: {self._cpp}점>'
    
    def get_total(self):    
        return self._py+self._cpp

    def __ge__(self, other): 
        return self.get_total()>=other.get_total()
    def __lt__(self, other): 
        return self.get_total()<other.get_total()
        
    def get_name(self): 
        return self._name
        
def student_test1(): 
    pororo = Student('뽀로로', 10, 10)
    print(pororo)
# student_test1()    

def student_test2(): 
    with open('scores.csv', 'rt') as f: 
        parsed = csv.reader(f)
        next(parsed)
        next(parsed)
        # 학생 객체 리스트 생성 1: 리스트 축약
        lst = [Student(x[0], int(x[2]), int(x[4])) for x in parsed]
        
        # 학생 객체 리스트 생성 2: 객체 생성 후 리스트에 하나씩 추가
        # lst = []
        # for x in parsed:
            # name, _, py, _, cpp = x #unpackin 이 방식은 아래와 같이 리스트 축약에서도 사용 가능
            # std = Student(name, int(py), int(cpp)) 
            # lst.append(std)
            
            
        # 학생 객체 리스트 생성 3: 리스트 축약과 언패킹 조합 
        # lst = [Student(name, int(py), int(cpp))  for name, _, py, _, cpp in parsed]
        
        
    print(lst)
# student_test2()    

def student_test3(): 
    with open('scores.csv', 'rt') as f: 
        parsed = csv.reader(f)
        next(parsed)
        next(parsed)
        lst = [Student(x[0], int(x[2]), int(x[4])) for x in parsed]
        
    print(f'{lst[0].get_name()}의 총점 >= {lst[1].get_name()}의 총점:', lst[0]>=lst[1])
    
    print('총점 순 내림차순 정렬:', sorted(lst, reverse = True))
    highest = max(lst)
    print(f'최고득점자: {highest.get_name()}(총점 {highest.get_total()}점)')
    
# student_test3()    