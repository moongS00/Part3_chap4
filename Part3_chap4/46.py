# 근사값 알고리즘
'''
BMI출력 프로그램
'''

bmi = [18.5, 23, 25]
l_res = ['저체중', '정상', '과체중']
u_res = ['정상', '과체중', '비만']

uw = float(input('체중 입력(kg) : '))
uh = float(input('신장 입력(m) : '))

ubmi = round(uw / (uh * uh), 2)
print(f'사용자bmi : {ubmi}')
dif = []

for i in bmi:
    dif.append(round(ubmi - i, 2))

minD = 50
minI = 0
for i, n in enumerate(dif):
    if minD > abs(n):
        minD = n
        minI = i


if minD < 0:
    print(f'결과 : {l_res[minI]}')
elif minD > 0:
    print(f'결과 : {u_res[minI]}')
