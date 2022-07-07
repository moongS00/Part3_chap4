# 최대값
'''
최대값 알고리즘을 이용해 리스트에서 최대값과 최대값의 개수를 찾는 모듈 만들기
리스트는 1-50에서 난수 30개, 중복 허용
'''

def findMaxNum(ns):
    mn = ns[0]
    cnt = 0

    for i in ns:
        if i > mn:
            mn = i

    for i in ns:
        if i == mn:
            cnt += 1

    return mn, cnt


import random

nums = []
for i in range(30):
    a = random.randint(1, 50)
    nums.append(a)

print(f'nums : {nums}')

res = findMaxNum(nums)
print(f'최대값 : {res[0]}')
print(f'최대값 개수 : {res[1]}')