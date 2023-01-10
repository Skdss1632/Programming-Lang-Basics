# Written a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, returning an empty string "".
class Solution:

    def longest_common_prefix(self, strs):
        common_prefix = ''
        string_0 = strs[0]
        index1 = 0
        for i in string_0:
            count_common_e = 0
            for j in range(1, len(strs)):
                if i in strs[j][index1]:
                    count_common_e += 1
                    if count_common_e == len(strs)-1:
                        common_prefix = common_prefix+i
                        index1 += 1
            if count_common_e == 0:
                break
        return f"'{common_prefix}'"


s1 = Solution()
final_output = s1.longest_common_prefix(["flower", "flow", "flight"])
print(final_output)