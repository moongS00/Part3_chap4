# 최빈값 알고리즘
'''
최빈값 알고리즘을 이용한 나이 분포 그래프 출력
'''

ages = [25, 27, 27, 24, 31, 34, 33, 31, 27, 25, 45, 37, 38, 46, 47, 22, 24,
        29, 33, 35, 27, 34, 37, 40, 42, 29, 27, 25, 26, 27, 31, 31, 32, 38, 25, 27, 28, 40, 41, 34]

def FindMaxNum(ns):
    maN = 0

    for n in ns:
        if n > maN:
            maN = n

    print(f'최고령자 : {maN}세')

    return maN


def CntGraph(ns):
    maxNum = FindMaxNum(ns)
    cnt = [0 for i in range(maxNum + 1)]

    for a in ns:
        cnt[a] += 1

    print(f'나이 분포 : {cnt}')
    k = round(1, -3)
    for i, n in enumerate(cnt):

        if n != 0:
            print(f'[{k}] {i}세 빈도수 : {n}\t', end='')
            print('+' * n)
            k += 1


if __name__ == '__main__':
    print(f'직원 수 : {len(ages)}명')
    CntGraph(ages)