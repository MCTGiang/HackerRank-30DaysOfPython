--Task
--Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative; if a negative argument is passed as initialAge, the constructor should set age to 0 and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
--1.yearPasses() should increase the age instance variable by 1.
--2.amIOld() should perform the following conditional actions:
--If age < 13, print You are young..
--If age >= 13 and age < 18, print You are a teenager..
--Otherwise, print You are old..
--To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. 
--The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge >= 0:
           self.age = initialAge
        else:
            self.age = 0
            print('Age is not valid, setting age to 0.') 
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print('You are young.')
        elif 13 <= self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
