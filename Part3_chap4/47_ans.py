class NumSum:
    def __init__(self, n1, n2):
        self.bigNum = 0
        self.smallNum = 0
        self.setN1N2(n1, n2)

    def setN1N2(self, n1, n2):
        self.bigNum = n1
        self.smallNum = n2

        if n1 < n2:
            self.bigNum = n2
            self.smallNum = n1

    def addNum(self, n):    # n부터 1까지의 합
        if n <= 1:
            return n

        return n + self.addNum(n-1)

    def sumBetweenNums(self):
        return self.addNum(self.bigNum-1) - self.addNum(self.smallNum)