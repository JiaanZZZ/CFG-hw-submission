"""
Two Sum
-------------------------------------------------------------------------------------------------------------------------
Given an array of integers nums and an integer target, return two numbers inside that array such that they add up to target.

You may assume that each input would have at least one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLE 1:
---------------------------------------------------------------
Input: nums = [2,7,11,15], target = 9
Output: [2, 7]
Explanation: Because nums[0] + nums[1] == 9, we return [2, 7].

EXAMPLE 2:
---------------------------------------------------------------
Input: nums = [3,2,4], target = 6
Output: [2, 4]

EXAMPLE 3:
---------------------------------------------------------------
Input: nums = [3,3], target = 6
Output: [3, 3]

NOTES:
---------------------------------------------------------------
- An input MAY HAVE no two numbers at all (an empty one still counts as a solution) - in this case, return a empty array
- It's an array of integer numbers - these numbers are not necessarily distinct / unique
- Make sure to discuss your solution - what is the Big O Time & Space complexity? Was there anyway you could've done...
...better or not? Why or why not? Justify.
"""


def twoSum(numbers, target):
    answer_set=set()
    answer_list=[]
    for num in numbers:
        if target-num in answer_set:
            answer_list.append(target-num)
            answer_list.append(num)
            return answer_list
        answer_set.add(num)
    return answer_list

"""
Space complexity: O(n)
There is a set and a list created. The space complexity is dependent on the length of numbers 
for the worst case. There can be no matching answers so all the numbers needed to be stored in set

Time complexity: O(n)
There is only one loop in the function. The worst case is to loop through all the elements in the numbers.

"""
        

