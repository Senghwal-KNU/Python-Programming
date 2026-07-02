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
replace_5_24()

def replace_1():
    
def list_test1():
    #리스트에 멤버 추가하기: append(원소) / insert(인덱스,원소) / extend(컬렉션;리스트,range 등..)
    #제거: pop(인덱스):인자 생략시 마지막 원소 제거, 제거 원소 반환, remove(원소):원소없으면 오류발생
    
    #리스트 섞기- random모듈의 shuffle()사용  
    
def list_method_3():
    