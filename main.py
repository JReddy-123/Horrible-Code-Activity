class Calculator:
<<<<<<< HEAD
   def __init__(self):
       pass


   def add(self, x, y):
       return float(x) + float(y)


   def multiply(self, x, y):
       return x * y


   def divide(self, dividend, divisor):
       return dividend / divisor


   def remainder(self, dividend, divisor):
       return dividend % divisor


=======
    def __init__(self):
        pass
>>>>>>> b2cbc8eb87f3dfa9bcacf807bae4abb0752d6bc0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, dividend, divisor):
        return dividend / divisor


def main():
<<<<<<< HEAD
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
           print("Provide the dividend: ")
           operand_1 = float(input())
           print("Provide the divisor: ")
           operand_2 = float(input())
           print(calculator.divide(operand_1, operand_2))
       elif user_input == "off":
           print("Turning off the calculator")
           break
=======
    calculator = Calculator()
    while True:
        print("What would you like? (add, subtract, multiply, divide, off)")
        user_input = input()
        if user_input == "add":
            print("Provide the 1st number you would like to add: ")
            operand_1 = input()
            print("Provide the 2nd number you would like to add: ")
            operand_2 = input()
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
            print("Provide the dividend: ")
            operand_1 = float(input())
            print("Provide the divisor: ")
            operand_2 = float(input())
            print(calculator.divide(operand_1, operand_2))
        elif user_input == "off":
            print("Turning off the calculator")

>>>>>>> b2cbc8eb87f3dfa9bcacf807bae4abb0752d6bc0

main()