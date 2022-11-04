# November 4 2022
print("##############################################################")
# Binary Search
def binarySearch(array, x, low, high):
    if high >= low:
         mid = low + (high - low)//2
        
        # if found at mid, then return it
    if array[mid] == x:
        return mid
    
        # Search the left half 
    elif array[mid] > x:
        return binarySearch(array, x, low, mid-1)
    
        # Search the right half
    else:
        return binarySearch(array,x,mid+1,high)

array = [3,4,5,6,7,8,9]
x = 4
result = binarySearch(array,x,0,len(array-1))

# Binary Search is a function to search through a list for a given value
# where a list is identified from the begining and the end then the middle point is found. 
    # then using if statements we search if the middle point is greater than or smaller than the given value and the list is shortened untill the value is found.
    # https://www.geeksforgeeks.org/binary-search/ , https://www.geeksforgeeks.org/python-program-for-binary-search/
    # cs.usfca.edu/~galles/visualization/Search.html 



#Iterative Apprach or Recursive Approach
print("##############################################################")
# Bubble Sorting #
# The Simpliest form of sorting in the system where-in two sequential values are compared with the smaller value being moved to the left side while the larger value is moved
# to the right side. The process is simple in that it iterates through multiple times until it is finally sorted.

def bubbleIter(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[i] > arr[i+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

data = [-2,45,0,11,-9]
print(data)
bubbleIter(data)
print(data)



#Insertion Sort Execution
# Going through a unsorted list and checking each value if they are less than the previous values
# if so it will continue down the list, otherwise it will be placed after the checked value.
        # a Value is checked against the previous values until it can no longer move to the left.

# A value is selected than ran through the list compaing against each element  c


def insertionSort(arr):
    for i in range(1, len(arr)): # For everything from the 1st index onwards
        key = arr[i] # Set key equal to arr[i]
        j = i -1 # j is the index i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = key

data 