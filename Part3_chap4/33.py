# 순위 알고리즘
'''
숫자로 이루어진 리스트에서 아이템의 순위를 출력하고, 순위에 따라 아이템을 정렬하는 모듈을 만들어보자.
리스트는 50-100 사이의 난수 20개를 이용하자.
'''
# 글러 먹은 풀이 (순위 구하는 방식이 틀림)

def getMaxNum(ns):
    maxNum = 0
    for n in ns:
        if n > maxNum:
            maxNum = n

    return maxNum


import random

def getRank(ns):
    mn = getMaxNum(ns)

    idx = [0 for i in range(mn+1)]

    for n in ns:
        idx[n] += 1

    idx = idx[49:]
    print(f'ranks : {idx}')

    sNums = []
    n = 0
    i = 0
    while n <= len(idx):
        if idx[i] == n:
            sNums.append(idx[n])
        n += 1
        i += 1

    print(f'sNums : {sNums}')


nums = random.sample(range(50, 101), 20)
getRank(nums)