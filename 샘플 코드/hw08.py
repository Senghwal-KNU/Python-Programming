import string
import random


def hw08_1(): 
    target = random.sample(range(1, 11), 3)
    
    print('Debugging hint:', target)
    
    while True: 
        usr = [int(x) for x in input('복권번호 3개: ').split()]
        in_range_usr = [x for x in usr if 1<= x<=10]
        no_dup_usr = set(usr) #사용자 입력에서 중복 제거 
        
        err_cnt = 0
        if len(usr)!= 3: 
            err_cnt += 1
            print('[입력오류] 번호 3개를 입력해주세요.') 
        if len(in_range_usr)!= len(usr): #3이 아니라 len(usr)랑 비교해야함.  
            err_cnt += 2
            print('[입력오류] 범위 내의 값을 입력해주세요.') 
        if len(no_dup_usr) != len(usr):
            err_cnt += 4
            print('[입력오류] 중복없이 입력해주세요.') 
        if err_cnt == 0: 
            break
    
    hit_cnt = 0
    for x in target: 
        if x in usr: 
            hit_cnt += 1
            
    if hit_cnt == 3: 
        print('1억원')
    elif hit_cnt == 2: 
        print('1천만원')
    elif hit_cnt == 1: 
        print('1만원')
    else: 
        print('다음 기회에...')
 
# hw08_1()

def hw08_2(): 
    lst = ['dog', 'cat', 'tiger', 'lion']
    n = int(input('n: '))
    
    rot_cnt = n%len(lst) 
    
    for _ in range(rot_cnt): 
        lst.insert(0, lst.pop())
        
    print(f'오른쪽으로 {n}칸 로테이션: {lst}')
  
# hw08_2()


def get_words(msg): 
    for x in string.punctuation: 
        msg = msg.replace(x, ' ')
    return msg.split()
    

def hw08_3(): 
    usr = input('문장: ')
    rslt = get_words(usr)
    if rslt: 
        print('문장에 포함된 단어:', ', '.join(rslt))
    else: 
        print('문장에 포함된 단어가 없습니다. ')
    
# hw08_3()

def get_distinct_words(msg):  
    for x in string.punctuation: 
        msg = msg.replace(x, ' ')
    
    words = msg.split()
    
    no_dup = []    
    no_dup_lower = []    
    
    for x in words: 
        if x.lower() not in no_dup_lower: 
            no_dup_lower.append(x.lower())
            no_dup.append(x)
    
    return no_dup
    

def hw08_3_1(): 
    msg = input('문장: ')
    rslt = get_distinct_words(msg)
    
    if rslt: #if len(rslt)!=0: 
        print('문장에 포함된 단어:', ', '.join(rslt))
    else: 
        print('문장에 포함된 단어가 없습니다. ')
    
# hw08_3_1()

def hw08_4(): 
    msg = input('문장: ').lower()

    for x in string.punctuation: 
        msg = msg.replace(x, ' ')

    words = msg.split()

    keyword = input('검색할 단어: ').strip()
    cnt = words.count(keyword.lower())
    
    print(f'{keyword} 검색 횟수: {cnt}')


# hw08_4()



def hw08_4_1(): 
    msg = input('문장: ')
    org = msg #원문은 보관해두고, msg를 조작
    
    #구두점 제거 -> 단어분리 
    for x in string.punctuation: 
        msg = msg.replace(x, ' ')
    words = msg.split()

    keywords = input('검색할 단어: ').strip()
    lower_keywords = keywords.lower()
    hit_words = [] #검색한 단어 저장
    
    for x in words: 
        if x.lower() == lower_keywords: 
            hit_words.append(x)
            
    rslt = ', '.join(hit_words)
    if hit_words: 
        print(f"'{org}' 문장에서 '{keywords}' 검색 횟수: {len(hit_words)} ({rslt})")
    else: 
        print(f"'{org}' 문장에서 '{keywords}'가 검색되지 않았습니다.")
    


# hw08_4_1()


def gen_anagram(words): 
    letters = list(words) #문자열은 shuffle()불가 ->리스트로 캐스팅후 셔플
    random.shuffle(letters)
    anagram = ''.join(letters)
    return anagram

def hw08_5(): 
    while True: 
        tmp = input('단어: ').split()
        if len(tmp) == 1: 
            word = tmp.pop() # word = tmp[0]
            break
        else: 
            print('[입력오류] 단어 한 개를 입력해주세요. ')
    ana = gen_anagram(word)
    print(f'{word}의 애너그램: {ana}')

# hw08_5()





