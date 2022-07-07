# 병합정렬 : 자료구조를 분할하고 각각 분할된 자료구조를 정렬하면서 병합
'''
리스트를 선택정렬 알고리즘을 이용해 오름차순, 내림차순 정렬 하기
정렬 과정도 로그로 출력
'''
# 선생님 풀이(여전히 이해 못함)

def sortMerge(ns, asc = True):

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    left_nums = sortMerge(ns[0:midIdx], asc=asc)
    right_nums = sortMerge(ns[midIdx:len(ns)], asc=asc)

    merge_nums = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_nums) and right_idx < len(right_nums):

        if asc:
            if left_nums[left_idx] < right_nums[right_idx]:
                merge_nums.append(left_nums[left_idx])
                left_idx += 1

            else:
                merge_nums.append(right_nums[right_idx])
                right_idx += 1

        else:
            if left_nums[left_idx] > right_nums[right_idx]:
                merge_nums.append(left_nums[left_idx])
                left_idx += 1

            else:
                merge_nums.append(right_nums[right_idx])
                right_idx += 1


    merge_nums += left_nums[left_idx:]
    merge_nums += right_nums[right_idx:]

    print(f'merge_nums : {merge_nums}')
    return merge_nums



import random

nums = random.sample(range(1, 21), 10)
print(f'nums : {nums}')
a = sortMerge(nums)
print(f'오름차순 정렬 후 : {a}')
print()
d = sortMerge(nums, asc=False)
print(f'내림차순 정렬 후 : {d}')
