# 최소값 알고리즘
'''
학급 전체 학생의 시험 점수에 대한 평균과 최소값을 구하고
평균과 최소값의 편차를 출력하는 프로그램을 최소값 알고리즘을 이용해 만들어보자
'''
def getMinNum(ns):
    min_num = ns[0]
    total_num = 0

    for n in ns:
        total_num += n
        if n < min_num:
            min_num = n

    avg_num = total_num / len(ns)
    sub_num = round(avg_num - min_num, 2)

    print(f'평균 : {avg_num}')
    print(f'최소값 : {min_num}')
    print(f'편차 : {sub_num}')

scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]
getMinNum(scores)