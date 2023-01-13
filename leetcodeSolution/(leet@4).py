# Given an integer x, returning true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        l1 = []  # empty list 1
        l2 = []  # empty list 2
        while x > 0:
            reverse = x % 10  # reversing int value
            l1.append(reverse)  # appending reverse value in l1
            x = x // 10
        for i in range(len(l1) - 1, -1, -1):  # loop for appending value in l2
            l2.append(l1[i])   # appending reverse value in l2
        if l1 == [] and l2 == [] and x != 0:  # if x is negative int
            # then both list will empty that's why I use condition here
            return False
        elif l1 == l2 or x == 0:  # here is condition for:- if x is not a negative int then I compare l1 and l2
            return True
        else:
            return False


s1 = Solution()
result = s1.isPalindrome(10)
print(result)