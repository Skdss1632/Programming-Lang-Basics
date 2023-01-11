# Given a string s consisting of words and spaces, returning the length of the last word in the string.
class Solution:

    def lengthOfLastWord(self, s: str):
        new_str = s.strip()  # removing the leading and trailing whitespace:-'fly me   to   the moon'
        list_of_str = new_str.split(' ')  # list of the strings['fly', 'me', 'to', 'the', 'moon']
        return len(list_of_str[-1])  # returning the len of the last word


s1 = Solution()
result = s1.lengthOfLastWord('fly me   to   the moon    ')
print(result)