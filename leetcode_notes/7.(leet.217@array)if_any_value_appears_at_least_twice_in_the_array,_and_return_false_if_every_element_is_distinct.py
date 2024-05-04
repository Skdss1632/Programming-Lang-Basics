# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


s1 = Solution()
result = s1.containsDuplicate([1, 3, 4, 5, 3])
print(result)
# ........................................................................................................................

# 2nd approach

# class Solution(object):
#     def containsDuplicate(self, nums):
#         return len(set(nums)) < len(nums)
# ........................................................................................................................

# 3rd approach

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         return False if len(nums) == len(list(set(nums))) else True

