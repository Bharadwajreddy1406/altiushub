def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        

    return max(dp)



l = list(map(int,input().split()))

print(l)
print(length_of_lis(l))



# 🧑‍💻 Intern (0–1 Years Experience) 
# Given an integer array nums, return the length of the longest strictly increasing subsequence. Come up with an algorithm that runs in O(n log(n)) time complexity

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 
# Constraints:
# •	1 <= nums.length <= 2500
# •	-104 <= nums[i] <= 104
# Focus Areas:
# •	Dynamic Programming
# •	Binary Search
# •	Time and space optimisation


