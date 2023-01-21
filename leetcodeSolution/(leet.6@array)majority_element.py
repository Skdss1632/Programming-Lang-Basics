"""Given an array nums of size n, return the majority element.The majority element is the element that appears
more than [n / 2] times."""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        for ele in set(nums):
            if nums.count(ele) > len(nums)/2:
                return ele


s1 = Solution()
result = s1.majorityElement([2, 2, 1, 1, 1, 2, 2])
print(result)