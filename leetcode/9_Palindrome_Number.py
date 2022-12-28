class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = ''
        for n in range(len(str(x))-1, -1, -1):
            y = y + str(x)[n]
        return y == str(x)
#  36.51%


if __name__ == '__main__':
    x = 12121
    answer = Solution()
    print(answer.isPalindrome(x))


#  решение из комментов, 94%
        # x=str(x)
        # for i in range(len(x)//2):
        #     if x[i]!=x[-i-1]:
        #         return False
        # return True  