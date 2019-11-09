class Calc:
    # def __init__(self, a, b, *args):
    #     self.a = a
    #     self.b = b
    #     self.args = args

    def add(self, a, b, *args):
        sum = 0
        for x in args:
            sum += x
        return sum + a + b

    def sub(self, a, b, *args):
        sum = 0
        for x in args:
            sum += x
        return a - b - sum

    def mul(self, a, b, *args):
        sum = 1
        for x in args:
            sum = sum * x
        return a * b * sum

    def div(self, a, b, *args):
        sum = 1
        for x in args:
            sum = sum * x
        return a / b / sum


if __name__ == '__main__':
    ca = Calc()
    temp = ca.add(1, 2, 3, 4)
    print(temp)
    temp2 = ca.sub(1, 2, 3, 4)
    print(temp2)
    temp3 = ca.mul(2, 3, 5)
    print(temp3)
    temp4 = ca.div(105, 5, 3)
    print(temp4)

