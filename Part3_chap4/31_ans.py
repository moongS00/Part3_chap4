import lineMod
import random

if __name__ == "__main__":

    rNums = random.sample(range(1, 21), 10)
    searchNum = int(input('찾으려는 숫자 입력 : '))

    resIdx = lineMod.searchNum(rNums, searchNum)

    if resIdx == -1:
        print('No Result Found')
        print(f'Search result Index : {resIdx}')

    else:
        print('>>Search Results<<')
        print(f'Search result Index : {resIdx}')
        print(f'Search result number : {rNums[resIdx]}')



