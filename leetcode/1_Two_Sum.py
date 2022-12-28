class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            copy = nums[i+1::]
            if x in copy:
                return[i, copy.index(x)+i+1]


if __name__ == '__main__':
    nums = [3,3]
    target = 6
    answer = Solution()
    print(answer.twoSum(nums, target))

    
# >>> alist = ['foo', 'spam', 'egg', 'foo']
# >>> foo_indexes = [n for n,x in enumerate(alist) if x=='foo']
# >>> foo_indexes
# [0, 3]
# >>>

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# class Solution(object):
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i] + nums[j]  == target:
#                     return(i,j)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
# 	# while iterating through every num, we store them as key and it's index as value in seen.
# 	# At the same time we check if (target-num) is present in seen's keys, if yes
# 	# we simply return that number's index from seen and the current number's index. That's it.
#         seen = {}
#         for idx, num in enumerate(nums):
#             if target-num in seen:
#                 return [seen[target-num], idx]
#             seen[num] = idx