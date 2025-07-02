"""Program1-Calulator"""

class Calculator:
    def __init__(self,a,b):
        self.a=float(a)
        self.b=float(b)
    def Add(self):
        print("Addition:",self.a + self.b)
    def Subtract(self):
        print("Subtraction:",self.a - self.b)
    def Multiply(self):
        print("Multiplication:",self.a * self.b)
    def Div(self):
        if self.b != 0:
            print("Division:",self.a / self.b)
        else:
            print("Error: Division by zero")


s = input("Enter Operator:")
a = input("Enter a:")
b = input("Enter b:")
Calculate = Calculator(a, b)

if s == '+':
    Calculate.Add()
elif s == '-':
    Calculate.Subtract()
elif s == '*':
    Calculate.Multiply()
elif s == '/':
    Calculate.Div()
else:
    print("Invalid Operator.!")




