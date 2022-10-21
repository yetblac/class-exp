# October 21 2022
# Print will show a value Meanwhile a return will call a function then use
# a Function to then complete a predetermined task to produce a result 
print("##############################################################")
##############################################################
#                       Recursion
############################################################## 
# Recursion is similar to a unbounded loop 
# To best show Recursion we will use Factorials as an example
        # Remeber 0! is equal to 1
# Recusion is calling a function within that same function. Maybe???
# Recursion is made up of two major components
        # The Stopping Point (The Base Case)
        # The Loop (The Inductive Step)

    # The Inductive step will seve to 
        # Understand what to do with the data
        # How to make the Data smaller


def factorial(n):
    if n == 0:
        return 1 
    else:
        return n * factorial(n-1)

# The Above program is utilized to first, check if the inputed value is equal to 0, if so it will return 1
# Otherwise it will take the value given, then multiply that number by the sum of factorial(n-1)
        # Please observe that the Recursion takes place during the return statement as such it is completelted before being looped.
print(factorial(5)) 
# The above should return 120,

print("##############################################################")


# We can look into another example where we are trying to find only the intigers in a list of elements
def onlyInt(xlst):
    if xlst == []:
        return []
    elif type(xlst[0]) !=int:
        return [] + onlyInt(xlst[1:])
    else:
        return [xlst[0]] + onlyInt(xlst[1:])

print(onlyInt([1,3,4,5,'9','10',15]))

# In the above function we are taking the list and first checking if the list is empty if it is, it will return a empty list
# Next it indexs through the lst checking for if the element is NOT equal to an integer if it is, the element is added to an empty lst.
# The recursion happens next wherein we take call the defined function with the same list EXECPT we only go from the 1st index onwards
            # for example if the intial list is [1,2,3,4] xlst[1:] will change the intial list to [2,3,4]


# HOWEVER if the element is a integer, the element is returned in a list PLUS the function will run again until the list is empty.

print("##############################################################")

##############################################################
#                       Tail Recursion
############################################################## 

# Tail Recursion has the primary objective of spreading out problem solving instead of all processing occuring at the end of a program
# The Argument will oftentimes be the smae as regular recursion however it will include a accumulator
# the Accumulator is returned when the base level is achieved.

# For example to find a factorial using Tail Recursion it will look like this

def tfact(n, a=1):
    if n == 0:
        return a
    else:
        return tfact(n-1, a = a * n)

print(tfact(5))

print("##############################################################")
# in this case the base case is defined already so when n == 0 it just returns the accumulator which is the answer by the end.
# the accumulator can be set to the result desired by a edgecase
# In the case above a is inreasing with every recursion through the function. 
# finally when n == 0, a will be equal to the desired result.

# to apply this to onlyInts 

def tailOnlyInt(xlist, a = []):
    if xlist == []:
        return a
    elif type(xlist[0]) != int:
        return [] + tailOnlyInt(xlist[1:],a = [])
    else:
        return [xlist[0]] + tailOnlyInt(xlist[1:],a = [])



# The above is my attempt at this

# below is the actual correct method

def tailOnlyCorrect(clst, a = []):
    if clst == []:
        return a
    elif type(clst[0]) != int:
        return tailOnlyCorrect(clst[1:], a =a) # when the element is not an integer the list is simply sliced and the unwanted element is removed, meanwhile a stays the same.
    else:
        return tailOnlyCorrect(clst[1:], a = a + [clst[0]]) # once a value is confirmed to be a integer it is then stored into a with a = a + [clst[0]]

print(tailOnlyCorrect([13,'a',45,'yo',15,16,17,'swamp']))

# The major point is that a is being updated as the program continues as such when clst is sliced to be empty it returns what a has been stored with.

print("##############################################################")

##############################################################
#                       Memoization
############################################################## 

# The Technique of saving values that have already been computed
# This will ensure you are not doubling computing and instead saving outputs
# for example in our brains when we do 5 * 4 * 3 = ?
        # we will store that 3 * 4 = 12 then take 12 * 5 = 60
        # the act of storing the 12 to save time is the same of memoization


d = {}
def memoFact(n):
    if n not in d.keys():
        if n == 1:
            d[n] = 1
        else:
            d[n] = n * memoFact(n-1) # d[n] = n * memoFact(n-1) or if n = 5  # 5! or d[5] = 5 * 4!. In this case 4! will continue through the loop
    return d[n]

# in the above function we first check to see if n is a key in the dictonary, if it isnt, we will then check if n == 1
    # if so d[n] or the answer is 1
# otherwise we will set d[n] which is esentially, 
                # {n : n!}
        # We are setting a value key to its corresponding factorial


print(memoFact(5))

print("##############################################################")


