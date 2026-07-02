def str_method():
    #format()
    print('{}|{}|{}|{}|{}'.format(1,2,3,4,5))
    
    #replace(old,new)
    st='hello, world! hello python!'
    st.replace('hello','hi')
    print('st:',st)
    print('st.replace:',st.replace('hello','hi'))
    st=st.replace('hello','hi')
    print('대입 후 st:',st)
# str_method()

def replace_11_16():
    test_list = ['No. 224', 'No. 587', 'No. 29', 'No. 37']
    
    # lst=[x.replace('No. ','') for x in test_list]
    # num_list=[int(x) for x in lst]
    # ↓ 한 줄로 축약 가능
    lst=[int(x.replace('No. ','')) for x in test_list]
    
    print('num_list =',lst)
# replace_11_16()

def replace_3():
    
    usr1=input("오늘의 지출: ").split()   #2만원 8900 145천원 9500
    usr1=[x.replace('만원','0000').replace('천원','000') for x in usr1]
    usr1=[int(x) for x in usr1]
    # ↓ replace 먼저도 가능
    usr2=input('오늘의 지출: ').replace('만원','0000').replace('천원','000').split()
    usr2=[int(x) for x in usr2]
    
    n_usr=usr2
    
    print(f'총 {len(n_usr)}회 지출 총액은 {sum(n_usr):,}원이고, 회당 평균 지출은 {sum(n_usr)/len(n_usr):,.2f}원입니다.')
# replace_3()
    
def replace_5_24():
    import string
    st=input('문장: ')
    
    for s in string.punctuation:
        st=st.replace(s,' ')
    
    lst=st.split()
    
    #정렬 sorted(list) 사용
    print('사전식 정렬 후:',', '.join(sorted(lst)))
    print('사전식 역정렬 후:',', '.join(sorted(lst,reverse=True)))
    print('사전식 역정렬 후:',', '.join(sorted(lst)[::-1]))
    print('길이별 정렬 후:',', '.join(sorted(lst,key=len)))
# replace_5_24()

def replace_1():
    pass
    
def list_test1():
    #리스트에 멤버 추가하기: append(원소) / insert(인덱스,원소) / extend(컬렉션;리스트,range 등..)
    #제거: pop(인덱스):인자 생략시 마지막 원소 제거, 제거 원소 반환, remove(원소):원소없으면 오류발생
    
    #리스트 섞기- random모듈의 shuffle(list)사용  
    
    #count(값): 값과 같은 원소 개수 반환, 없으면 0 / index(원소): 원소 처음 발견된 위치 반환, 없으면 오류발생
    
    #lst.sort():반환값 없음,원본변경 vs sorted(list):반환값 있음,원본유지
    pass
    
def list_method_3():
    lst=[]
    while True:    
        usr=input("정수: ")
        if usr.lower()=='stop':
            break
        elif int(usr)%2==0:
            lst.append(int(usr))
            
    str_lst=[str(x) for x in lst]
    if len(str_lst)!=0:
        print('입력 값 중 짝수들:',', '.join(str_lst))
    else:
        print('입력 값 중에는 짝수가 없습니다.')
# list_method_3()

def list_method_4():
    usr=input("오늘의 지출: ").split()
    print(usr)
    
    rslt=[]
    
    for s in usr:
        print(s)
        if s.isdecimal():
            rslt.append(int(s))
        else:
            idx=rslt.index('원')
            flt=float(s[:idx-1])
            won=s[idx-1]
            if won=='만':
                rslt.append(flt*10000)
            if won=='천':
                rslt.append(flt*1000)
    
    print(f'총 {len(rlst)}회 지출 총액은 {sum(rslt):,}원이고, 회당 평균 지출은 {sum(rslt)/len(rslt):,.2f}원입니다.')
list_method_4()

def list_method_5_danger(): # 위험한 코드
    #입력받아서 split, 리스트 성분 중 'by, in, the, of, for, and' 있으면 remove()
    words=input('문자열: ').split()
    del_words='by,in,the,of,for,and'.split()
    
    for x in words:
        if x in del_words:
            words.remove(x) # for문에서 remove 사용하면 위험, 제거대상 빼고 새로 모아야함
            #왜? -> 성분 없애면 그 자리 채운다고 성분들이 이동하면서 for x 에 안잡히는 성분 생김
    rslt=[x[0].upper() for x in words]
    print(''.join(rslt))
# list_method_5_danger()

def list_method_5():
    words=input('문자열: ').split()
    del_lst='by,in,the,of,for,and'.split(',')
    # print(del_lst)
    
    lst=[]
    for x in words:
        if x not in del_lst:
            lst.append(x)
    
    rslt=[x[0].upper() for x in lst]
    print(''.join(rslt))

    lst2=[x[0].upper() for x in words if x not in del_lst]
    print(''.join(lst2))
# list_method_5()