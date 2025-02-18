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


main()