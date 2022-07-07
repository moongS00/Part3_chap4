ka = 88; ea = 82; ma = 90
sa = 78; ha = 92; aa = 86

hks = 85; hes = 90; hms = 82
hss = 88; hhs = 100
ha = round((hks + hes + hms + hss + hhs) / 5, 2)

s19kt = ka*20 - hks; s19et = ea*20 - hes; s19mt = ma*20 - hms
s19st = sa*20 - hss; s19ht = ha*20 - hhs; s19at = aa*20 - ha

s19ka = s19kt / 19 ; s19ea = s19et / 19 ; s19ma = s19mt / 19
s19sa = s19st / 19 ; s19ha = s19ht / 19; s19aa = s19at / 19


kg = hks - s19ka
eg = hes - s19ea
mg = hms - s19ma
sg = hss - s19sa
hg = hhs - s19ha
ag = ha - s19aa

print(f'국어 점수 차이 : {"+" + str(round(kg, 2)) if kg > 0 else round(kg, 2)}')
print(f'영어 점수 차이 : {"+" + str(round(eg, 2)) if eg > 0 else round(eg, 2)}')
print(f'수학 점수 차이 : {"+" + str(round(mg, 2)) if mg > 0 else round(mg, 2)}')
print(f'과학 점수 차이 : {"+" + str(round(sg, 2)) if sg > 0 else round(sg, 2)}')
print(f'국사 점수 차이 : {"+" + str(round(hg, 2)) if hg > 0 else round(hg, 2)}')
print(f'평균 차이 : {"+" + str(round(ag, 2)) if ag > 0 else round(ag, 2)}')

