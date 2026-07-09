'''st=dict(전자=1,컴공=2,경영=3,수학=4)
print('\n학과 번호',st)
for k in st:
    print('->{}:{:2d}번'.format(k,st[k]))
person={'이름':'홍길동','나이':26,'몸무게':'82'}
person['나이']='27'
print(person)
del person['나이']
print(person)
d1={'이름':'홍길동','나이':26}
d2={'나이':26,'이름':'홍길동'}
print(d1==d2)
person={'이름':'홍길동','나이':26,'몸무게':'82'}
print(person.keys())
print(person.values())
print(person.items())
print(person.get('취미'))
print(person.get('이름'))
student={202203:90, 202201:100, 202205:95}
print('\n',student)
for p in student:
    print('학번 {},{:3d}점'.format(p,student[p]))
print('\n',student)
for p in student.keys():
    print('학번 {},{:3d}점'.format(p,student[p]))
print('\n',student)
for p in student.values():
    print('{:3d}점'.format(p))
print('\n',student)
for p in student.items():
    print(p)
print('\n',student)
for k,v in student.items():
    print('학번 {},{:3d}점'.format(k,v))
season=dict(봄='spring', 여름='summer', 가을='autumn', 겨울='winter')
while True:
    str=input('알고 싶은 계절을 한글로 입력:')
    if str in season.keys():
        print('{} 영어 철자는 {}'.format(str,season[str]))
    else:
        print('{}는 없다'.format(str))
    ans=input('계속할까요(y/n)')
    if ans != 'y':
        break
print('Byebye')'''
import getpass
import warnings
warnings.filterwarnings('ignore')
upp=low=dig=pct=0
pswd=getpass.getpass('비번 입력:','')
if pswd.isalnum()==False:
    pct=1
for k in pswd:
    if k.isupper():
        upp=1
    elif 'a'<=k<='z':
        low=1
    elif k.isdigit():
        dig=1
if low+upp+dig+pct>=3:
    print('비번으로 사용가능')
else:
    print('비번으로 사용불가')
