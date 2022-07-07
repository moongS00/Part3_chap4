# 버블정렬 : : 인접한 두개의 값을 비교 해서 크기에 따라 위치를 서로 교환
'''
숫자로 이루어진 리스트를 버블정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈을 만들어보자
정렬 과정도 로그로 출력하기
'''

def sortBubble(ns, asc = True):
    ln = len(ns) - 1

    if asc:
        for i in range(ln):
            for j in range(ln - i):
                if ns[j] > ns[j + 1]:
                    ns[j], ns[j + 1] = ns[j + 1], ns[j]

            print(f'{i} : {ns}')
    else:
        for i in range(ln):
            for j in range(ln - i):
                if ns[j] < ns[j + 1]:
                    ns[j], ns[j + 1] = ns[j + 1], ns[j]

            print(f'{i} : {ns}')

    return ns

nums = [10, 4, 1, 13, 11, 16, 17, 14, 6, 5]
print(f'정렬 전 : {nums}')
a = sortBubble(nums)
print(f'오름차순 정렬 후 : {a}')
d = sortBubble(nums, asc=False)
print(f'내림차순 정렬 후  : {d}')

