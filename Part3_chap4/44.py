# 순위 알고리즘
'''
알파벳 문자들과 정수들에 대한 순위를 정하는 프로그램
알파벳은 아스키코드 값을 이용
'''


def MakeAscII(d):
    ascIIDatas = []

    for n in d:
        if n == str(n):
            n = ord(n)

        ascIIDatas.append(n)
    print(f'ascIIDatas : {ascIIDatas}')
    return ascIIDatas


def getRank(d):
    asIIData = MakeAscII(d)
    ranks = [0 for i in range(len(asIIData))]

    for i in range(len(asIIData)):
        for j in range(len(asIIData)):
            if asIIData[i] < asIIData[j]:
                ranks[i] += 1

    print(f'ranks : {ranks}')
    return ranks


def printRank(d):
    res = getRank(d)

    for i, n in enumerate(d):
        print(f'data : {d[i]}\trank:{res[i] + 1}')

if __name__ == '__main__':
    datas = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']
    print(f'datas : {datas}')
    printRank(datas)
