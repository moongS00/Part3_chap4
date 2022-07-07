datas = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']
print(f'datas : {datas}')


ascIIDatas = []
for a in datas:
    if str(a).isalpha():
        ascIIDatas.append(ord((a)))
        continue

    ascIIDatas.append(a)
print(f'ascIIDatas : {ascIIDatas}')


ranks = [0 for i in range(len(ascIIDatas))]
for idx, n1 in enumerate(ascIIDatas):
    for n2 in ascIIDatas:
        if n1 < n2:
            ranks[idx] += 1
print(f'ranks : {ranks}')

for i, d in enumerate(datas):
    print(f'data : {datas[i]}\trank:{ranks[i] + 1}')