# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for element in set(nums):
            if nums.count(element) == 1:
                return element


s1 = Solution()
result = s1.singleNumber([2, 2, 1])
print(result)

# ..........................................................................................................................

# 2nd approach

# class Solution(object):
#     def singleNumber(self, nums):
#         # Initialize the unique number...
#         uniqNum = 0
#         # TRaverse all elements through the loop...
#         for idx in nums:
#             # Concept of XOR...
#             uniqNum ^= idx
#         return uniqNum       # Return the unique number...
#
# s1 = Solution()
# result = s1.singleNumber([2, 2, 1])
# print(result)

