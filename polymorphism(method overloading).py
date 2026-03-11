class Calculator:
    def add(self, a, b=0, c=0):
        result = a + b + c
        print("Sum =", result)

c = Calculator()

c.add(5, 3)
c.add(5, 3, 2)