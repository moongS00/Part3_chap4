# 최소값
'''
최소값 알고리즘을 이용해 리스트에서 최소값과 최소값의 개수를 찾는 모듈 만들기
리스트는 1-50에서 난수 30개, 중복 허용
'''


def findMinNum(ns):
    mn = ns[0]
    cnt = 0

    for i in ns:
        if i < mn:
            mn = i

    for i in ns:
        if i == mn:
            cnt += 1

    return mn, cnt


import random

nums = []
for i in range(30):
    nums.append(random.randint(1, 50))

print(f'nums : {nums}')

res = findMinNum(nums)
print(f'최소값 : {res[0]}')
print(f'최소값 개수 : {res[1]}')