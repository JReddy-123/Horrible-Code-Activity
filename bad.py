class Calculator:
   def __init__(self):
       pass


   def add(self, x, y):
       return x + y #Returns x + y


   def multiply(self, x, y):
       aLotOfAdding = 0 #aLotOfAdding =0

       for i in range(y):
           aLotOfAdding = x + aLotOfAdding
       return aLotOfAdding


   def divide(self, thisNumberDivideBy, thatNumber):
       return thisNumberDivideBy / thatNumber



   def remianderCalculations(self, dividend, divisor):
       # Bruh who wrote this code it is dumb
       return dividend % divisor


   def remainder(self,dividend, divisor):
       #gets remainder using remainder calcuations function
       return self.remianderCalculations(dividend, divisor)

   def sayHi(self):
       # prints "Hi Calculator user"
       print("Hi")
       print(" Calculator")
       print(" user")

   def sayBye(self):
       # prints "bye Calculator user"
       print("Bye")
       print(" Calculator")
       print(" user")






#what does main even do
def main(): #this is main
   calculator = Calculator()
   while True:
       print("What would you like? (add, subtract, multiply, divide, off)")
       a = input()
       if a == "add":#user input
           #ask user to provide the 1st number they would like to add
           print("add number")
           operand_1 = float(input())
           # ask user to provide the 1st number they would like to add
           print("add number")
           operand_2 = float(input())
           print(calculator.add(operand_1, operand_2))
       elif a == "subtract":#user input
           #ask user to provide the 1st number they would like to subtract
           print("Provide number ")
           operand_1 = float(input())
           # ask user to provide the 2nd number they would like to subtract
           print("Provide another number ")
           operand_2 = float(input())
           print(calculator.subtract(operand_1, operand_2))
       elif a == "remainder":#user input
           #Ask user to Provide the 1st number they would like to multiply
           print("Provide number ")
           operand_1 = float(input())
           # Ask user to Provide the 1st number they would like to multiply
           print("Provide number ")
           operand_2 = float(input())
           print(calculator.remainder(operand_1, operand_2))
       elif a == "divide": #user input
           #have user provide dividen
           print("Provide the number: ")
           operand_1 = float(input())
           # have user provide divider
           print("Provide the number: ")
           operand_2 = float(input())
           print(calculator.divide(operand_1, operand_2))
       elif a == "off":#user input
           print("Turning off the calculator")
           break
main()
