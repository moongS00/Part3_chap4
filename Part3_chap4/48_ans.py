# 최대값 알고리즘
'''
학급 전체 학생의 시험 점수에 대한 평균과 최대값을 구하고
평균과 최대값의 편차를 출력하는 프로그램
'''
scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]


def getAvg(ns):

    total = 0
    for n in ns:
        total += n

    return round(total / len(ns), 2)


def getMax(ns):

    mN = ns[0]
    for n in ns:
        if n > mN:
            mN = n

    return mN


def getDeviation(n1, n2):

    return abs(n1 - n2)