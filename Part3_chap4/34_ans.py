import minMod

scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]
sc_avg = minMod.getAvg(scores)
sc_min = minMod.getMin(scores)
sc_dev = minMod.getDeviation(sc_avg, sc_min)

print(f'평균 : {sc_avg}')
print(f'최소값 : {sc_min}')
print(f'편차 : {sc_dev}')