# 삽입정렬 알고리즘
'''
삽입정렬 알고리즘을 이용해 오름차순, 내림차순 정렬 하기
정렬 과정도 로그로 출력
'''
import copy
import random
def sortInsert(ns, asc = True):
    c_ns = copy.copy(ns)
    print(f'정렬 전 : {c_ns}')

    if asc :
        for i in range(len(c_ns) ):
            for j in range(0, i):
                if c_ns[i] < c_ns[j]:
                    c_ns[i], c_ns[j] = c_ns[j], c_ns[i]
            print(f'{i}회 : {c_ns}')

    else:
        for i in range(len(c_ns)):
            for j in range(0, i):
                if c_ns[i] > c_ns[j]:
                    c_ns[i], c_ns[j] = c_ns[j], c_ns[i]
            print(f'{i}회 : {c_ns}')


    return c_ns


nums = random.sample(range(1, 21), 10)
a = sortInsert(nums)
print(f'오름차순 정렬 후 : {a}')
print()
d = sortInsert(nums, asc=False)
print(f'내림차순 정렬 후 : {d}')