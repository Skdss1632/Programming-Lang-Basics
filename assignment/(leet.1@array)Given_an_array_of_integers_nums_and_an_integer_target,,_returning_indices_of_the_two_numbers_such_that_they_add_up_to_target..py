# Given an array of integers nums and an integer target,
# returning indices of the two numbers such that they add up to target.

class Solution:
    def twosum(self, nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


s1 = Solution()
x = s1.twosum([2, 2], 4)
print(x)
