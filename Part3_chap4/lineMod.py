def searchNum(ns, sn):

    resultIdx = -1

    print(f'Numbers : {ns}')
    print(f'Searvh Numbers : {sn}')

    n = 0
    while True:
        if n == len(ns):
            print('Search Fail!')
            break

        elif ns[n] == sn:
            resultIdx = n
            print('Search Success!')
            print(f'Search result Index : {resultIdx}')
            break

        n += 1

    return resultIdx