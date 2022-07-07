import binaryMod

if __name__ == '__main__':
    nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]
    searchNum = int(input('input search number : '))

    resIdx = binaryMod.searchNum(nums, searchNum)
    print(f'nums : {nums}')

    if resIdx == -1:
        print('No Result Found')
        print(f'Search result Index : {resIdx}')

    else:
        print('>>Search Results<<')
        print(f'Search result Index : {resIdx}')
        print(f'Search result number : {nums[resIdx]}')