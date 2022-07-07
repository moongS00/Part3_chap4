class LottoMode:

    def __init__(self, ln):
        self.lottoNums = ln
        self.modeList = [0 for n in range(1, 47)]

    def getCnt(self):

        for n in self.lottoNums:
            for num in n:
                self.modeList[num] += 1

        return self.modeList

    def ModeList(self):
        if sum(self.modeList) == 0:
            return None

        for i, m in enumerate(self.modeList):
            if i != 0:
                print(f'번호 : {i}, 빈도 : {m}, ', end='')
                print('*' * m)