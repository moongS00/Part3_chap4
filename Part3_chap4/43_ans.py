# 클래스 너무 많이 만들어서 그냥 내꺼에 빈도수 정렬 방법만 붙임

ages = [25, 27, 27, 24, 31, 34, 33, 31, 27, 25, 45, 37, 38, 46, 47, 22, 24,
        29, 33, 35, 27, 34, 37, 40, 42, 29, 27, 25, 26, 27, 31, 31, 32, 38, 25, 27, 28, 40, 41, 34]


def FindMaxIdx(ns):
    maN = 0
    maI = 0

    for i, n in enumerate(ns):
        if n > maN:
            maN = n
            maI = i

    return maI, maN

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

    n = 1
    while True:
        res = FindMaxIdx(cnt)
        maxNum = res[1]
        maxIdx = res[0]

        if maxNum == 0:
                break

        print(f'[{n:0>3}] {maxIdx}세 빈도수 : {maxNum}\t', end='')
        print('+' * maxNum)

        cnt[maxIdx] = 0

        n += 1




if __name__ == '__main__':
    print(f'직원 수 : {len(ages)}명')
    CntGraph(ages)