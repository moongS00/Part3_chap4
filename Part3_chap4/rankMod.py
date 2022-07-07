def getRank(ns):

    ranks = [0 for i in range(len(ns))]

    for idx, n1 in enumerate(ns):
        for n2 in ns:
            if n1 < n2:
                ranks[idx] += 1

    print(f'nums : {ns}')
    print(f'ranks : {ranks}')

    # 순위 출력
    for i, n in enumerate(ns):
        print(f'num : {n}\trank : {ranks[i] + 1}')

    # 순위에 따라 리스트 재정렬
    sortedNums = [0 for n in range(len(ns))]
    for idx, rank in enumerate(ranks):
        sortedNums[rank] = ns[idx]


    return sortedNums