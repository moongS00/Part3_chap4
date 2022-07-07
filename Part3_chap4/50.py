# 평균 알고리즘
'''
홍길동 학생을 제외한 나머지 학생의 평균과 홍길동 학생의 점수 차이를 출력하는 프로그램
출력은 과목별 점수와 평균 점수를 모두 출력
'''




def AVG(ns):
    total = 0

    for n in ns:
        total += n

    return round(total / len(ns) , 2)

def DIFF(ns):
    total = [88, 82, 90, 78, 92, 86]

    dif = []

    for i, n in enumerate(ns):
        if (n - total[i]) < 0:
            dif.append(round(n - total[i], 2))

        elif (n - total[i]) > 0:
            dif.append('+' + str(round(n - total[i], 2)))

    return dif


if __name__ == '__main__':
    hong = [85, 90, 82, 88, 100]
    hong.append(AVG(hong))

    d = DIFF(hong)
    print(f'차이 : {d}')