import random
import rankMod

if __name__ == '__main__':

    nums = random.sample(range(50, 101), 20)
    sNums = rankMod.getRank(nums)
    print(f'sNums : {sNums}')