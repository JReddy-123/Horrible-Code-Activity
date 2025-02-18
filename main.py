class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, dividend, divisor):
        return dividend / divisor


def main():
   calculator = Calculator()
   while True:
       print("What would you like? (add, subtract, multiply, divide, off)")
       user_input = input()
       if user_input == "add":
           print("Provide the 1st number you would like to add: ")
           operand_1 = float(input())
           print("Provide the 2nd number you would like to add: ")
           operand_2 = float(input())
           print(calculator.add(operand_1, operand_2))
       elif user_input == "subtract":
           print("Provide the 1st number you would like to subtract: ")
           operand_1 = float(input())
           print("Provide the 2nd number you would like to subtract: ")
           operand_2 = float(input())
           print(calculator.subtract(operand_1, operand_2))
       elif user_input == "multiply":
           print("Provide the 1st number you would like to multiply: ")
           operand_1 = float(input())
           print("Provide the 2nd number you would like to multiply: ")
           operand_2 = float(input())
           print(calculator.multiply(operand_1, operand_2))
       elif user_input == "divide":
           print("Provide the dividend: ") # The number being divided
           operand_1 = float(input())
           print("Provide the divisor: ") # The number to divide by
           operand_2 = float(input())
           print(calculator.divide(operand_1, operand_2))
       elif user_input == "off":
           print("Turning off the calculator")
           break # Exits while loop so that program can terminate


main()