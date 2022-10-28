# October 28 2022
# Lab 7 COMPLETE
print("##############################################################")
##############################################################
#                       Paths
############################################################## 
# Absolute Path:
# The adress at the top of the file directory in the explorer such as C:\Users\yetson\desktop ** IMPORTANTLY STARTS FROM THE ROOT FILE such as "C:" or "/"
# This will tell a program where something is located on THIS LOCAL MACHINE

# Relative Path
# The Aress of a program relative to where it orginates from
# This will tell a program where something is located relative meaning it can be used on different systems.
##############################################################
#                       List Comprehension
############################################################## 
# or a Inline for Loops
print([2*i for i in range(4)])
# The Above will return [0,2,4,6]
# In the above case it will first find i in range of 4
# This will give 0,1,2,3.
    # These values will then be set through a given operation, in this case 2*i
    # as such it returns [ 0*2, 1*2, 2*2, 3*2 ]
print("##############################################################")
# We can also use multiple for loops 
print([(i,j) for i in range(4) for j in range(3)])
# is the same as
# for k in range(4):
#     for h in range(3):
    
#         print([(k,h)])
print("##############################################################")

# We can also filter using if statements
print([i for i in range(10) if i%3==0])
# In the above you can see that the function is setting i to i (i for i) within the range, if and only if i/3 = 0
print("##############################################################")
##############################################################
#                       Strip & Split
############################################################## 
# Strip
print('www.example.com'.strip('cmowa.'))
# The function will work from both ends starting with the leadin  w and last m, it will check if the letters are in the given strip parameter,
# if so it will be removed after performing this until it can no longer, in the given example we will end with 'example'
# Important the strip function cannot jump over letters as such 'a' cannot be stripped as 'e' and 'x' block the function
print("##############################################################")
# Split
print('J e t s o n B l a c k'.split())
# The function will take the given string then split the string on the given parameter
print("##############################################################")
print('Jetson,Black,Is,In,class'.split(','))
print("##############################################################")
# The output of a split function will always return a list. as such you can index the list to find the nth word in a sentance or phrase.
print(''.split('\ '))
print("##############################################################")
# \n is a parameter used to define a NEW LINE
# This is an example\n
# To see new lines 
print('07\n25\n2022'.splitlines())
print("##############################################################") 