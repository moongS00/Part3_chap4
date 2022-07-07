# 근사값 알고리즘
'''
근사값 알고리즘을 이용해 수심 입력 시 수온 출력하는 모듈 제작
'''

depth = [0, 5, 10, 15, 20, 25, 30]
temper = [24, 22, 20, 16, 13, 10, 6]

input_depth = int(input('input depth : '))

dif = []

for i in depth:
    dif.append(abs(i - input_depth))
print(f'dif : {dif}')

mintem = dif[0]
minIdx = 0

for i, n in enumerate(dif):
    if n < mintem:
        mintem = n
        minIdx = i

print(f'mintem : {mintem}, minIdx : {minIdx}')

watwertem = temper[minIdx]

print(f'depth : {input_depth}m')
print(f'watwer temperature : {watwertem}도')