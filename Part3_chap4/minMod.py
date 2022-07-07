def getAvg(ns):

    total = 0
    for n in ns:
        total += n

    return  total / len(ns)


def getMin(ns):
    min_num = ns[0]

    for n in ns:
        if n < min_num:
            min_num = n

    return min_num


def getDeviation(n1, n2):
    return round(abs(n1 - n2), 2)



def getMaxOrMin(ns, maxFlag=True):  #최대, 최소값을 구하는 함수를 하나로 만듦
    res = ns[0]
    
    if maxFlag:
        for n in ns:
            if n > res:
                res = n
    else:
        for n in ns:
            if n < res:
                res = n
                
    return res