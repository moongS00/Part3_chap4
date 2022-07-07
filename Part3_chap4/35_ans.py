import random
import bubbleMod

if __name__ == '__main__':
    nums = random.sample(range(1, 21), 10)
    print(f'정렬 전 : {nums}')

    a = bubbleMod.sortBubble(nums)
    print(f'오름차순 정렬 후 : {a}')

    d = bubbleMod.sortBubble(nums, asc=False)
    print(f'내림차순 정렬 후  : {d}')