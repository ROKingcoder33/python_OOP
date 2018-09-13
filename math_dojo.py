class MathDojo(object):
    def __init__(self):
        self.sum = 0

    def add(self, *num):
        for i in range(0, len(num)):
            if type(num[i]) == list or type(num[i]) == tuple:
                for n in num[i]:
                    self.sum += n
            else:
                self.sum += num[i]
        return self

    def subtract(self, *num):
        for i in range(0, len(num)):
            if type(num[i]) == list or type(num[i]) == tuple:
                for n in num[i]:
                    self.sum -= n
            else:
                self.sum -= num[i]
        return self

    def result(self):
        print("The total is " + str(self.sum))
        return self

md = MathDojo()
md.add(2).add(2,5,1).subtract(3,2).result()
