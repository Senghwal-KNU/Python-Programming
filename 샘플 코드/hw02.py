def gen_list(): 
    #리스트 생성법 1: 원소 나열
    lst = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(lst) 
    #리스트 생성법 2: 캐스팅: range, str--> list로 형변환
    a = range(2, 21, 2)
    lst = list(a)
    print(lst)
    #리스트 생성법 3: 리스트 축약
    lst = [x*2 for x in range(1, 11)]
    print(lst)
    
def averagePositive():
    nums = [float(x) for x in input('실수 여러 개(쉼표로 구분): ').split(',')]
    positive = [x for x in nums if x>0]
    print(f'입력한 수 중 양수는 {positive}입니다. 총 {len(positive)}개의 평균은 {sum(positive)/len(positive)}입니다.')
    
def multiples4(): 
    n = int(input('4 이상의 정수: '))
    rslt = list(range(4, n+1, 4))
    print(f'{n} 이하의 4의 배수는 {rslt}입니다. ')
    
def atob():
    a, b = [int(x) for x in input('두 정수(공백으로 구분): ').split()]
    rslt = range(a, b+1)
    print(f'{a} 이상 {b} 이하의 정수: {list(rslt)}')
    print(f'합: {sum(rslt)}')
    
def power_test():
    base = int(input('밑: '))
    a, b = [int(x) for x in input('지수 2개(공백으로 구분): ').split()]
    rslt = [base**x for x in range(a, b+1)]
    print(f'{base}의 {a}제곱 ~ {b}제곱: {rslt}')

def max_min_sorted_test(): 
     lst = [float(x) for x in input('실수 여러 개: ').split()]
     print('최댓값:', max(lst))
     print('최솟값:', min(lst))
     print('오름차순 정렬 결과:', sorted(lst))