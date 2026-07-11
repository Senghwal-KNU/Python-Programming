def mungu_store(): 
    dct = {'공책': 1000, '연필': 500, '지우개': 500, '볼펜': 1000}
    '''
    items = '공책 연필 지우개 볼펜'.split()
    prices = [int(x) for x in '1000 500 500 1000'.split()]
    dct = dict(zip(items, prices))
    '''
    print('{:3s}\t{:5s}'.format('품목', '가격'))
    print('*'*15)
    for x in dct: 
        print('{:3s}\t{:5,d}원'.format(x, dct[x]))
    print()
        
# mungu_store()

def mungu_store_1(): 
    dct = {'공책': 1000, '연필': 500, '지우개': 500, '볼펜': 1000}
    print('취급 품목(총 {}개): {}'.format(len(dct), ', '.join(dct))) 
# mungu_store_1()

def mungu_store_2(): 
    dct = {'공책': 1000, '연필': 500, '지우개': 500, '볼펜': 1000}
    cart = {}#빈 딕셔너리 
    
    while True: 
        item = input('상품: ').strip()
        if item =='나가기':
            break
        if item in dct: 
            if item in cart: 
                cart[item] += 1
            else: 
                cart[item] = 1
                
            #위 코드와 같은 문장 1
            ''' 
            if item not in cart:
                cart[item]  = 0
            cart[item] += 1
            '''
            
            # 위 코드와 같은 문장 2: pythonic code(파이썬다운 코드)
            # cart[item]  = cart.get(item, 0)+1
            
            print(f'{item}을 장바구니에 담았습니다. ')
        else: 
            print(f'{item}은 취급하지 않습니다. ')
            
    print()
    print('*'*15)
    print('장바구니 내역')
    for x in cart: 
        print('{}(주문 수량: {})'.format(x, cart[x]))
        
    total = 0
    for x in cart: 
        total += dct[x] * cart[x]
        
    print(f'주문 금액: {total:,}원')

# mungu_store_2()

def alpha_freq(): 
    dct = {} #빈 딕셔너리 생성

    while True:
        st = input('문장: ').strip()
        if st.lower() == 'stop': 
            break
            
        tmp = [x.lower() for x in st if x.isalpha() == True]
        for x in tmp: 
            if x in dct: 
                dct[x] += 1
            else: 
                dct[x] = 1
                
    for x in dct: 
        print(f'{x}: {dct[x]}')
        
alpha_freq()