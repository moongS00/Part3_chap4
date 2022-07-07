def searchNum(ns, sn):

    reslutIdx = -1

    staIdx = 0
    endIdx = len(ns) - 1
    midIdx = (staIdx + endIdx) // 2
    midVal = ns[midIdx]

    print(f'staIdx : {staIdx}, endIdx : {endIdx}')
    print(f'midIdx : {midIdx}, midVal : {midVal}')

    while sn >= ns[0] and sn <= ns[len(ns) - 1]:

        if sn == ns[len(ns) - 1]:
            reslutIdx = len(ns) - 1
            break

        if staIdx + 1 == endIdx:
            if ns[staIdx] != sn and ns[endIdx] != sn:
                break


        if sn > midVal:
            staIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'+staIdx : {staIdx}, endIdx : {endIdx}')
            print(f'+midIdx : {midIdx}, midVal : {midVal}')

        elif sn < midVal:
            endIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = ns[midIdx]
            print(f'-staIdx : {staIdx}, endIdx : {endIdx}')
            print(f'-midIdx : {midIdx}, midVal : {midVal}')

        elif sn == midVal:
            reslutIdx = midIdx
            break

    return reslutIdx