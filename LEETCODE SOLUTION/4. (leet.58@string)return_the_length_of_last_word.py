# Given a string s consisting of words and spaces, returning the length of the last word in the string.
class Solution:

    def lengthOfLastWord(self, s: str):
        # remove the leading and trailing whitespace:-'fly me   to   the moon'
        trimmed_string = s.strip()
        # Split the string into a list of words['fly', 'me', 'to', 'the', 'moon']
        words_list = trimmed_string.split(' ')
        # return the len of the last word
        return len(words_list[-1])


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