import random
import insertMod


if __name__ == '__main__':
    nums = random.sample(range(1, 21), 10)
    print(f'정렬 전 : {nums}')

    a = insertMod.sortInsert(nums)
    print(f'오름차순 정렬 후 : {a}')

    d = insertMod.sortInsert(nums, asc=False)
    print(f'내림차순 정렬 후  : {d}')