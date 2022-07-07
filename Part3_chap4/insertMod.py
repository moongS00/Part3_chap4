import copy

def sortInsert(ns, asc = True):
    c_ns = copy.copy(ns)
    for i1 in range(1, len(c_ns)):
        i2 = i1 - 1
        c_num = c_ns[i1]

        if asc:
            while (c_ns[i2] > c_num) and (i2 >= 0):
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1

            c_ns[i2 + 1] = c_num

        else:
            while (c_ns[i2] < c_num) and (i2 >= 0):
                c_ns[i2 + 1] = c_ns[i2]
                i2 -= 1


        c_ns[i2 + 1] = c_num
        print(f'c_ns : {c_ns}')

    return c_ns