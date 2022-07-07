sales = [12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]

def saleUpAndDown(ss):

    if len(ss) == 1:
        return ss

    print(f'sales : {ss}')

    cur_sale = ss.pop(0)
    next_sale = ss[0]

    dif = next_sale - cur_sale
    if dif > 0:
        dif = '+' + str(dif)
    print(f'매출 증감액 : {dif}')
    saleUpAndDown(ss)


if __name__ == '__main__':
    saleUpAndDown(sales)