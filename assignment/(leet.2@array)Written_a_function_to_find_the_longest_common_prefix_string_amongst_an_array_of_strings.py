# Written a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, returning an empty string "".
class Solution:

    def longest_common_prefix(self, strs):
        common_prefix = ''
        string_0 = strs[0]
        index1 = 0
        for letter in string_0:
            count_common_e = 0
            for j in range(1, len(strs)):
                if letter in strs[j][index1]:
                    count_common_e += 1
                    if count_common_e == len(strs)-1:
                        common_prefix = common_prefix+letter
                        index1 += 1
            if count_common_e == 0:
                break
        return f'longest common prefix is:- {common_prefix}'


s1 = Solution()
commonprefix = s1.longest_common_prefix(["fl", "flight"])
print(commonprefix)
# ........................................................................................................................

# 2nd approach

# class Solution:
#
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         result = ""
#         for i in zip(*strs):
#             if len(set(i)) == 1:
#                 result += i[0]
#             else:
#                 return result
#
#
# s1 = Solution()
# x = s1.longestCommonPrefix(["flower", "flower", "flight"])
# print(x)


