### Code Sample 1

Time: O(n) There is one for loop in the codes which means the time increases when the length of numbers increases.
Space: O(n) There is an extra set created in the code, Since we are looping through the numbers and each number will be put into set if there is no matching number.

### Problem Sample 2

Time: O(N) Since we are doing recursive traversal, when we start with node a, we are actually going to look at the node b and node c. The number of child nodes of b/c must be smaller than the number of child nodes of a. For each height, the same rules applies. So the max time needed is to traverse all the nodes which is O(N)

Space: O(h) h is the height of the tree since we need a stack to store the child nodes for both sides.

### Code Sample 3
Time: O(n) Since the left pointer starts at 0 and right pointer starts at the end of the string. For the worst case, two pointers need to move towards to the middle point to prove the string is palindrome. Therefore the lenghth of the string matters which leads to O(n)

Space: O(1) which is a constant value. There is no additional storage needed since no other variable is created so the space complexity is constant.

### Problem Sample 4

Time: 
    - The best case is O(1) because the target value if exactly the middle point 
    - For the worst case O(logn) because every time half of the search array will be disposed so the length is 1/2 of previous searched array.

Space: O(1). There is no additional storage objects created to store any value.

