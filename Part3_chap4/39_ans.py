class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumCnt = 0

    def setMaxNum(self):
        self.maxNum = 0

        for n in self.nums:
            if self.maxNum < n:
                self.maxNum = n


    def getMaxNum(self):
        self.setMaxNum()
        return self.maxNum

    def setMaxCnt(self):
        self.setMaxNum()

        for n in self.nums:
            if self.maxNum == n:
                self.maxNumCnt += 1

    def getMaxCnt(self):
        self.setMaxCnt()
        return self.maxNumCnt

import random

nums = []
for i in range(30):
    a = random.randint(1, 50)
    nums.append(a)

print(f'nums : {nums}')

res = MaxAlgorithm(nums)
print(f'최대값 : {res.getMaxNum()}')
print(f'최대값 개수 : {res.getMaxCnt()}')