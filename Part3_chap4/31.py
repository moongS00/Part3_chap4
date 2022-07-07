# 선형검색 알고리즘(1)
'''
숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들어보자
1. 검색 모듈은 선형 검색 알고리즘을 이용
2. 리스트는 1부터 20까지의 정수 중 난수 10개
3. 검색 과정을 로그로 출력
4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없다면 -1을 출력
'''
def searchNum(n):

    import random
    numbers = random.sample(range(1, 21), 10)
    print(f'numbers : {numbers}')
    searchIndex = -1

    i = 0
    while True:
        if i == len(numbers):
            print('Search Fail!')
            print(f'Search result Index : {searchIndex}')
            break

        elif numbers[i] == n:
            searchIndex = i
            print('Search Success!')
            print(f'Search result Index : {searchIndex}')
            break

        i += 1

    print('>>Search Results')
    print(f'Search result Index : {searchIndex}')
    print(f'Search result number : {n}')


inputNum = int(input('찾으려는 숫자 입력 : '))
searchNum(inputNum)



