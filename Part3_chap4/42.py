# 재귀 알고리즘
'''
재귀 알고리즘을 사용해 1월 부터 12월 까지 전월 대비 매출 증감액을 나타내는 프로그램 만들기
'''

sales = [12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]

def FuncSales(lm):
    if len(lm) < 2:
        return  lm

    else:
        print(f'sales : {lm}')
        dif = lm[1] - lm[0]
        if dif > 0:
            print(f'매출 증감액 : +{dif}')
        else:
            print(f'매출 증감액 : {dif}')

        lm = lm[1:len(lm)]
        FuncSales(lm)



FuncSales(sales)