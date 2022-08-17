"""
Algorithms 1 Solution
-------------------------------------------------------------------------------------------------------------------------
"""
from unittest import result


def isValidSubsequence(array, sequence):
    sq_i=0
    for num in array:
        if sq_i==len(sequence):
            break
        if sequence[sq_i]==num:
            sq_i+=1
        

    return sq_i==len(sequence)

# Time complexity is O(n) since for the worst case we need to loop through the whole array
#  and array must be longer than the length of sequence.
# Space complexity is O(1) since we do not create any extra space to store any value.


    

# Some test cases are included in order to help you test your solution
# Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# As a result, make sure to think up some on your own and test your code as well!

# Sample Tests for Algorithms 1
# ---------------------------------------------------------
array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]
print(isValidSubsequence(array1, sequence1))  # FALSE

array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]
print(isValidSubsequence(array2, sequence2))  # TRUE

array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]
print(isValidSubsequence(array3, sequence3))  # TRUE

"""
Algorithms 2 Solution
-------------------------------------------------------------------------------------------------------------------------
"""
def findThreeLargestNumbers(array):
    first=-float('inf')
    second=-float('inf')
    third=-float('inf')

    for num in array:
        if num>first:
            third=second
            second=first
            first=num
        elif num>second:
            third=second
            second=num
        elif num >third:
            third=num
    result=[]
    result.append(third)
    result.append(second)
    result.append(first)
    

    return result
    

# Time complexity: O(n) We need to loop through the whole array to find three largest numbers
# Space complexity: O(1) only a result array is created to store three values which is always constant

# Some test cases are included in order to help you test your solution
# Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# As a result, make sure to think up some on your own and test your code as well!

# Sample Tests for Algorithms 2
# ---------------------------------------------------------
array1 = [141, 1, 17, -17, -27, 18, 541, 8, 7, 7]
expectedOutput1 = [18, 141, 541]
print(str(findThreeLargestNumbers(array1)) + " <-- --> " + str(expectedOutput1))  # [18, 141, 541]

array2 = [141, 1, 214, -17, -27, 0, 541, 21, 7, 34]
expectedOutput2 = [141, 214, 541]
print(str(findThreeLargestNumbers(array2)) + " <-- --> " + str(expectedOutput2))  # [141, 214, 541]

