# 최빈값 알고리즘
'''
다음은 회차별 로또 번호이다.
최빈도 알고리즘을 이용해 모든 회차의 각 번호에 대한 빈도수를 출력하는 프로그램
'''
import random
cnt = [0 for i in range(46)]
#print(cnt)

lottery = []
for i in range(30):
    temp = random.sample(range(1, 46), 6)
    lottery.append(temp)

for i in lottery:
    for j in i:
        cnt[j] += 1

for i in range(1, len(cnt)):
    if i != 0:
        print(f'번호 : {i}, 빈도 : {cnt[i]}, ', end='')
        print('*' * cnt[i])
