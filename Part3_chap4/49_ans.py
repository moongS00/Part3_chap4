ranks = [9.12, 8.95, 8.12, 6.9, 6.18]
scores = [6.7, 5.9, 8.1, 7.9, 6.7, 7.3, 7.2, 8.2, 6.2, 5.8]
print(f'scores : {scores}')


class MaxAlgorithm:

    def __init__(self, ss):
        self.scores = ss
        self.maxScore = 0
        self.maxIdx = 0


    def delMax(self):
        self.maxScore = self.scores[0]

        for i, s, in enumerate(self.scores):
            if self.maxScore < s:
                self.maxScore = s
                self.maxIdx = i

        print(f'self.maxScore : {self.maxScore}, self.maxIdx : {self.maxIdx}')

        self.scores.pop(self.maxIdx)
        print(f'self.scores : {self.scores}')


class MinAlgorithm:

    def __init__(self, ss):
        self.scores = ss
        self.minScore = 0
        self.minIdx = 0

    def delMin(self):
        self.minScore = self.scores[0]

        for i, s, in enumerate(self.scores):
            if self.minScore < s:
                self.minScore = s
                self.minIdx = i

        print(f'self.maxScore : {self.minScore}, self.maxIdx : {self.minIdx}')

        self.scores.pop(self.minIdx)
        print(f'self.scores : {self.scores}')


class TopPlayers:

    def __init__(self, cs, ns):
        self.curScore = cs
        self.newScore = ns

    def setAlignScore(self):
        nearIdx = 0
        minNum = 10.0

        for i, s in enumerate(self.curScore):
            abNum = abs(self.newScore - s)

            if abNum < minNum:
                minNum = abNum
                nearIdx = i

        if self.newScore >= self.curScore[nearIdx]:
            for i in range(len(self.curScore) - 1, nearIdx, -1):
                self.curScore[i] = self.curScore[i-1]
            self.curScore[nearIdx] = self.newScore

        else:
            for i in range(len(self.curScore) - 1, nearIdx+1, -1):
                self.curScore[i] = self.curScore[i-1]
            self.curScore[nearIdx+1] = self.newScore