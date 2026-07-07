def genOTP():
    import random
    
    otp=random.randint(0,999999)
    print(otp)
    
def people():
    person1 = ['온달', 20, 1, 180.0, 100.0]
    person2 = ['이사부', 25, 1, 170.0, 70.0]
    person3 = ['평강', 22, 0, 169.0, 60.0]
    person4 = ['혁거세', 40, 1, 150.0, 50.0]
    #인당 5개
    #이름, 나이, 성별, 키, 몸
    
    person_list=person1+person2+person3+person4
    
    def how_many_persons(person_list):
        n=len(person_list)/5
        return n
    
    n_persons=how_many_persons(person_list)
people()