# 재귀 알고리즘
'''
사용자가 정수 두개를 입력하면 작은 정수와 큰 정수 사이의 모든 정수의 합을 구하는 프로그램
'''

def sumMod(n1, n2, total = 0):
    total += n2

    if n1 == n2:
        return total

    sumMod(n1, n2+1, total=total)

a1 = int(input('n1 : '))
a2 = int(input('n2 : '))
r = sumMod(a1, a2)
print(r)