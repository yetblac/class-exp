# November 11th 2022

# Object Oriented Languages and Usage
# Python is a mixed language in that it uses proceedural and object oriented
# Aspects
##############################################################
#                     Class and Objects
############################################################## 

# A class is a abstract method of declaring a concept of things
# Has its own predefined keyword being "class"

# class Class_name: # naming convention, capital first letter
#     # static class variable
#     staticVar = "someValue"

#     # Constructor
#     def __init__(self, instanceVar, ...): #__init__ makes the function a constructor
#         self.instanceVar = instanceVar
#         <body>

#     # static class function without self
#     def classFunc(...):
#         <body> 

#     # a normal function, with self
#     def instanceFunc(self, ...):
#         <body> 

class Lab(): # Declares Class Name
    def __init__(self, name): #Constructor
        self.name = name # Instance Variable 
                        # In this example; s.name = Jetson
    @staticmethod
    def test3(x,y):
        print(x + y)
    
    def test(a):
        print("hello")
        print(a.name)
        

    def test2(a):
        print("yeah")
        print(a.name)



s = Lab("Jetson") # Creating an object for the class
        # S gets pass into the "self" parameter and the "Jetson" to "name"
s.test() # Calls a function using the tag that identifies a certain object thus does not need a given arguement
print("##############################################################")
s.test2() 
print("##############################################################")
s.test3(1,2)

    
# The constructors serves to seperate and template static and instance variables
# For a static variable it must be placed above the constructor header







