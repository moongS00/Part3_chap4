import copy
def sortBubble(ns, asc = True):
    c_ns = copy.copy(ns)
    ln = len(c_ns) - 1

    if asc:
        for i in range(ln):
            for j in range(ln - i):
                if c_ns[j] > c_ns[j + 1]:
                    c_ns[j], c_ns[j + 1] = c_ns[j + 1], c_ns[j]

            print(f'{i}회 : {c_ns}')
    else:
        for i in range(ln):
            for j in range(ln - i):
                if c_ns[j] < c_ns[j + 1]:
                    c_ns[j], c_ns[j + 1] = c_ns[j + 1], c_ns[j]

            print(f'{i}회 : {c_ns}')

    return c_ns