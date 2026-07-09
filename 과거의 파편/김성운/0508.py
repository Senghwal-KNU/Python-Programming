'''import datetime as dt
print('오늘=',dt.datetime.now())
hundred=dt.timedelta(weeks=1)
plus100day=dt.datetime.now()+hundred
print('일주일 후=',plus100day)
import time
timestamp=time.time()
local_time=time.localtime(timestamp)
print(time.strftime('%Y-%m-%d %H:%M:%S',local_time))
import time
start_time=time.time()
print(1+2+3+4+5+6+7+8+9+10)
end_time=time.time()
gap=end_time-start_time
print('1부터 10까지의 합을 구하고 출력하는 시간: {:7.4f}초'.format(gap))
import keyboard
import time

input('게임을 시작하려면 s키를 누르세요')
start_time=time.time()
while True:
    print('10초가 지났다고 생각되면 press q')
    if keyboard.is_pressed('q'):
        break
end_time=time.time()
gap=end_time-start_time
print(int(gap))
if int(gap)==10:
    print('시간감각이 뛰어나네요')
else:
    print('시간감각이 꽝이네요')
import random as rd
lotto_list=list(range(1,46))
rd.shuffle(lotto_list)
lotto_list=rd.sample(lotto_list,6)
lotto_list.sort()
print('이번주의 추천 로또번호:',lotto_list)'''
import math
print('1!=',math.factorial(1))
