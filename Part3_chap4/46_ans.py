
uw = float(input('체중 입력(kg) : '))
uh = float(input('신장 입력(m) : '))


class BmiAlgorithm:

    def __init__(self, w, h):
        self.BMI = {18.5: ['저체중', '정상'], 23: ['정상', '과체중'], 25: ['과체중', '비만']}
        self.userWeight = w
        self.userHeight = h
        self.userBMI = 0
        self.userCondition = ''
        self.nearNum = 0
        self.minNum = 25

    def calBMI(self):
        self.userBMI = round(self.userWeight / (self.userHeight * self.userHeight), 2)
        print(f'userBMI : {self.userBMI}')

    def UserCondition(self):

        for n in self.BMI.keys():
            absNum = abs(n - self.userBMI)
            if absNum < self.minNum:
                self.minNum = absNum
                self.nearNum = n

        print(f'nearNum : {self.nearNum}')

        if self.userBMI <= self.nearNum:
            self.userCondition = self.BMI[self.nearNum][0]
        else:
            self.userCondition = self.BMI[self.nearNum][1]