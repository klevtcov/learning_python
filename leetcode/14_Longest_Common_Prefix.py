class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 


if __name__ == '__main__':
    test_str = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(test_str))

