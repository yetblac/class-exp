testString = "This is a String to Show Operations"
print(testString[1:6:2])


# in this example [1:6] is used to show "This I" 
 # then :2] skips every other character creating "hsi"

# The Above Section was review over strings and manipulation of Strings

# The folling Section will be a review of looping.
# Looping is one of the most important aspects of software engineering
# as such a majority of my work will revolve around this section.
# the term "For Loops" are what is called a "bounded" loop.


lstAnimal = ["cat","dog","hamster","goat","turtle"]
print(len(lstAnimal))


# Running this will result in 5, the amount of individual elements
# in the lst, however index is completely different as there are 
# 0-4 indexs in the lst


for i in range(len(lstAnimal)):
    print("The animal at index " + str(i), "is" + " " + lstAnimal[i])


# in this function we first define the range of the list,
# in this case 5 as derived eariler, instead of putting 5 we just used 
# the list itself as a parameter : range(len(lstAnimal))
# for every index within the defined range the print function will run.
# Also we used i as a variable used to loop through the lst
# in the next line we go through and print each animal through
# looping through the lst defined earlier
# the loop will complete the function, then start again,
# first checking if the index value exist, if so then it will for the 
# the function one more time.

# in a "for loop" the range is important to denote and contain a loop
# for example in the above function, we used the length of the lst as a 
# range so if the lst changes the range updates with in. However in a 
# Tuple using a static number works since a tuple does not change.

# if the range for example looks like range(1,5,2) and the values are
# 0,1,2,3,4,5 it will return 1,3
# the reasoning is that 0 is outside the range of 1:5 and then we are
# left with 1,2,3,4,5 then we skip every "2" indexs because of :2] 
# final result will be 1,3,5


