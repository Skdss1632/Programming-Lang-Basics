# Given a string s consisting of words and spaces, returning the length of the last word in the string.
class Solution:

    def lengthOfLastWord(self, s: str):
        new_str = s.strip()  # removing the leading and trailing whitespace:-'fly me   to   the moon'
        list_of_str = new_str.split(' ')  # list of the strings['fly', 'me', 'to', 'the', 'moon']
        return len(list_of_str[-1])  # returning the len of the last word


s1 = Solution()
result = s1.lengthOfLastWord('fly me   to   the moon    ')
print(result)

# ........................................................................................................................
# 2nd approach

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.split()
#         return len(words[-1])
#
#
# s1 = Solution()
# result = s1.lengthOfLastWord("   fly me   to   the moon  ")
# print(result)

# ........................................................................................................................
# 3rd approach

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         ans = s.split(" ")
#         for i in range(len(ans)):
#             if ans[-1] == '':
#                 ans.pop()
#             else:
#                 return len(ans[-1])
#
#
# s1 = Solution()
# result = s1.lengthOfLastWord(' fly me   to   the moon ')
# print(result)