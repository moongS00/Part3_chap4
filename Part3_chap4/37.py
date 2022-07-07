# 선택정렬 알고리즘 : 최소값을 찾아 첫번째 레코드에 두고, 다시 최솟값을 찾아 두번째 레코드 위치에 놓는 방식
'''
리스트를 선택정렬 알고리즘을 이용해 오름차순, 내림차순 정렬 하기
정렬 과정도 로그로 출력
'''
# 선생님 풀이도 나와 동일
import copy
import random


def sortSelection(ns, asc = True):
    c_ns = copy.copy(ns)

    if asc:
        for i in range(len(c_ns) - 1):
            minIdx = i

            for j in range(i + 1, len(c_ns)):
                if c_ns[minIdx] > c_ns[j]:
                    minIdx = j

            c_ns[i], c_ns[minIdx] = c_ns[minIdx], c_ns[i]
            print(f'c_ns : {c_ns}')
        return c_ns

    else:
        for i in range(len(c_ns) - 1):
            minIdx = i

            for j in range(i + 1, len(c_ns)):
                if c_ns[minIdx] < c_ns[j]:
                    minIdx = j

            c_ns[i], c_ns[minIdx] = c_ns[minIdx], c_ns[i]
            print(f'c_ns : {c_ns}')
        return c_ns





nums = random.sample(range(1, 21), 10)
print(f'nums : {nums}')
a = sortSelection(nums)
print(f'오름차순 정렬 후 : {a}')
print()
d = sortSelection(nums, asc=False)
print(f'내림차순 정렬 후 : {d}')