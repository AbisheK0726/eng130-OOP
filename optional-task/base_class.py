class Calculator:
    def __init__(self, number1, number2): # Self refers to the current instance of the class
        self.number1 = number1
        self.number2 = number2
    def add(self):
        return self.number1 + self.number2
    def sub(self):
        return self.number1 - self.number2
    def mul(self):
        return self.number1 * self.number2
    def div(self):
        return self.number1 / self.number2