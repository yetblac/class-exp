print("##############################################################")
# Lab 5 Notes.\
# Unbounded Loops ar  used when a programmer doesnt know how many times will be iterated through.
# the Loop will be continued to be looped until a condition is met.

i = 0
while True:
    # instead of writing a condition the Programmer just writes "True"
    if i == 4:
        print("We have now left the Loop")
        break
    print("This is being printed by the loop")
    i = i + 1 # This is written to increase I until it exceeds the condition set by the if statement
print("##############################################################")

# When using a unbounded loop it is neccessary for i = 0, unlike in a for loop.
        # to make the above function into a bounded loop;
for i in range(4):
    print("This is being Printed in by the loop")

# We will use the unbounded loops when we are unaware of how many our range is and how many times we have to iterate.

print("##############################################################")

lst = ['a','b','c','d','e','f']
var = ''
i = 0
while True:
    var = lst[i] # we are iterating through the lst and addding each iterable into var
    i = i + 1 # increasing the value of i in the previous line
    print(var) 
    if var == 'd': # if at any point var is set equal to the iteration 'd'
        break # ends the loop

print("##############################################################")

# to make the above loop bounded.
for item in lst: # for " " in the lst we will iterate the length of the list
    print(item) 
    if item == 'd': # again if the iterated object is 'd' we will break 
        break

print("##############################################################")



#elst = [4,2,6,7]
#newLst = []
#while elst: # makes the function iterate the entire length of elst
    #if elst[0]%2 == 0:
        #newLst = newLst + elst[0]
    #elst = elst[1:] # This will update elst from the 1st index value ('2') to the end of the list




elst = [4,2,6,7]
newLst = []

for num in elst:
    if num%2 == 0:
        newLst + newLst + [num]
print(newLst)

print("##############################################################")
##############################
print (" # Lambda Function # " )
##############################
print("##############################################################")

# to Declare a Lambda Function 
lambda x: (x**2)(5)
    # lambda (variable name): (Equation to ask variable) (What to set variable to) # The above function will return 25
print(lambda x: (x**2)(5))

# it is possible to use multiple variables
lambda x,y,z: (x**2 + 2*y -z)(5,6,7)

print(lambda x,y,z: (x**2 + 2*y -z)(5,6,7))
# We can also use lambda as a function varialbe
summination = (lambda num1,num2: (num1 + num2))
summination(3,5)

print(summination(3,5))

# This will return 8 as num1 = 3, num2  = 5 

# NOTE FOR THESE TO WORK MAKE SURE TO USE THIS IN A FUNCTION, NOTHING IS PRINTING BECAUSE I HAVENT PRINTED ANYTHING

print("##############################################################")
##############################
print (" # Modulo Operator # " )
##############################
print("##############################################################")

# Modulo Operator is used by '%' which is used to check the remainder of a divison
# For example

num1 = 10
num2 = 3
remain = num1%num2
print(remain)

print("##############################################################")
##############################
print (" # Integer Divison # " )
##############################
print("##############################################################")

print(5/2) # this is standard divison this will result 2.5

#However when using the '//' will round the the result DOWN to its closest whole number
        # even if the result is 2.99, '//' will result in 2.
print(107/9)
print(107//9)

