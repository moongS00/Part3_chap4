# 평균 알고리즘
'''
최대값, 최소값을 제외한 나머지 점수들의 평균을 구하고 순위를 정하는 알고리즘 만들기
'''


def getMax(ns):
    Max_N = ns[0]
    Max_I = 0

    for i, n in enumerate(ns):
        if n > Max_N:
            Max_N = n
            Max_I = i

    return Max_N, Max_I


def getMin(ns):
    Min_N = ns[0]
    Min_I = 0

    for i, n in enumerate(ns):
        if n < Min_N:
            Min_N = n
            Min_I = i

    return Min_N, Min_I

def getAvg(ns):
    mxI = getMax(ns)[0]
    miI = getMin(ns)[0]
    print(f'최고점 : {mxI}')
    print(f'최저점 : {miI}')

    tot = 0

    for n in ns:
        if n == miI or n == mxI:
            continue
        tot += n

    print(f'avg : {round(tot / (len(ns) - 2), 2)}')
    return round(tot / (len(ns) - 2), 2)



def getRank(ns):
    ranks = [9.12, 8.95, 8.12, 6.9, 6.18]

    avg = getAvg(ns)

    for i, n in enumerate(ranks):
        if n < avg:
            ranks[i] = avg
            break

    print(f'ranks : {ranks}')
    print(f'my ranks : {i+1}')


if __name__ == '__main__':
    scores = [6.7, 5.9, 8.1, 7.9, 6.7, 7.3, 7.2, 8.2, 6.2, 5.8]
    print(f'scores : {scores}')
    getRank(scores)