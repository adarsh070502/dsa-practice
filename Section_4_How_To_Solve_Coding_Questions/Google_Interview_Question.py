"""Given a array find the pair which equals to the given sum and return True if pair is found
else false.

Ex:
    1) arr = [1,3,4,6] sum: 8
        False
    2) arr = [1,2,4,4] sum: 8
        True
"""


# Brute Force Approach
def brute_force(arr, target):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(i+1, arr_len):
            if arr[i]+arr[j] == target:
                return True
    return False


arr1 = [1, 3, 4, 6]
arr2 = [1, 2, 4, 4]
target = 8
print(brute_force(arr1, target))
print(brute_force(arr2, target))

"""
This Works but the time complexity here is O(n^2). 

So next approach would be like 
1) Create a empty dictionary.
2) When you iterate through each element, find the diff = target - each_element. 
3) Now check if diff is present in the dictionary, If present return True. And at end of the loop if not 
    found return False.
    
The time complexity of this approach would be O(n). 
"""


def better_approach(arr, target):
    diff_dict = {}

    for ele in arr:
        diff = target - ele
        try:
            if diff_dict[diff]:
                return True
        except KeyError:
            diff_dict[diff] = True
            continue
    return False


arr1 = [1, 3, 4, 6]
arr2 = [1, 2, 4, 4]
target = 8
print(better_approach(arr1, target))
print(better_approach(arr2, target))