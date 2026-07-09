'''f=open('sample.txt','r',encoding= 'UTF8')
s=f.read()
print(s)

f.close()

f=open('hello.txt','r')
s=f.read(5)
print(s)
s=f.read(5)
print(s)

f.close

f=open('foo.txt','r')
s=f.readlines()
print(s)

f.close

f=open('foo.txt','r')
s=f.readline()
print(s,end='')
s=f.readline()
print(s)

f.close

infilename=input('자료 파일 이름: ')
outfilename=input('결과 저장 파일 이름: ')

infile=open(infilename,'r')
outfile=open(outfilename,'w')

tot=0;count=0

line=infile.readline()
while line!='':
    s=int(line)
    tot+=s;count+=1
    line=infile.readline()

outfile.write('총매출='+str(tot)+'\n')
outfile.write('평균 일매출='+str(tot/count))

infile.close();outfile.close()

f=open('foo.txt','a+')
f.write('This will be appended.\n')
f.write('This too.\n')

f.close()
with open('hello.txt', mode='w') as f:
    f.write('Hello world!')
with open('hello.txt','x') as f:
    f.write('Hi~~~')
import csv
f=open('G:/score.csv',encoding='UTF8')
data=csv.reader(f)

header=next(data)
for row in data:
    print(row)
    avg=sum(map(int,row[1,4]))/len(row[1:4])
    print('평균:{:.2f}'.format(avg))

f.close()
infile=open("alphabet.txt","r+")
st=inflie.read(10);
print("읽은 문자열: ",st)
position=inflie.tell();
print("현재 위치: ",position)

position=inflie.seek(20)
str=inflie.read(5);
print("읽은 문자열: ",st)
infile.close()'''

import pickle as pk
month={1:'January',2:'February',3:'March',4:'April'}
month[5]='May'
month[6]='June'
lst=['pascal','python','java']

with open('month_data.bin', mode='wb') as f:
    pk.dump(month, f)
    pk.dump(lst, f)

print(' 바이너리 파일 쓰기 완료! '.center(30, '*'))

import pickle as pk
try:
    with open('month_data.bin',mode='rb') as f:
        dmon=pk.load(f)
        pl=pk.load(f)
except FileNotFoundError as e:
    print(e)
    print('파일 읽기 실패!'.center(30, '*'))
else:
    print(dmon)
    print(pl)
    print('바이너리 파일 읽기 완료!'.center(30,'*'))
finally:
    print('프로그램 종료!'.center(30,'*'))
