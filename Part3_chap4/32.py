# 이진검색 알고리즘
'''
숫자로 이루어진 리스트에서 사용자가 입력한 숫자를 검색하는 모듈을 다음 요건에 따라 만들어보자
1. 검색 모듈은 이진 검색 알고리즘을 이용
2. 리스트는 정해진 리스트 사용
3. 검색 과정을 로그로 출력
4. 검색에 성공하면 해당 정수의 인덱스를 출력하고, 검색 결과가 없다면 -1을 출력

이진 검색
    : 정렬되어 있는 자료구조에서 중앙값과의 크고 작음을 이용해서 데이터를 검색

데이터가 정렬되어 있어야 함!
'''

def searchNum(num):

    serachList = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
    serachList.sort()

    staIdx = 0
    endIdx = len(serachList) - 1
    midIdx = (staIdx + endIdx) // 2
    midVal = serachList[midIdx]

    resIdx = -1

    print(f'staIdx : {staIdx}, endIdx : {endIdx}')
    print(f'midIdx : {midIdx}, midVal : {midVal}')

    n = 0
    while True:
        if num > midVal:
            staIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = serachList[midIdx]
            print(f'+staIdx : {staIdx}, endIdx : {endIdx}')
            print(f'+midIdx : {midIdx}, midVal : {midVal}')
            print()

        elif num < midVal:
            endIdx = midIdx
            midIdx = (staIdx + endIdx) // 2
            midVal = serachList[midIdx]
            print(f'-staIdx : {staIdx}, endIdx : {endIdx}')
            print(f'-midIdx : {midIdx}, midVal : {midVal}')
            print()

        else:
            resIdx = midIdx
            print(f'serachList : {serachList}')
            print('>>Search Results<<')
            print(f'search result index : {resIdx}')
            print(f'search result number : {num}')
            break

        n += 1

        if n == len(serachList):
            print('Search Fail!')
            break



inputNum = int(input('input search number : '))
searchNum(inputNum)