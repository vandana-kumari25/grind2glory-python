class Solution(object):
    def findDisappearedNumbers(self, nums):
        seen = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)

        return result

nums = [4,3,2,7,8,2,3,1]

sol = Solution()

print(sol.findDisappearedNumbers(nums))

# def missingNumber(self, nums):
#         n = len(nums)

#         expected = n * (n + 1) // 2
#         actual = sum(nums)

#         return expected - actual


# return nums
# class Solution(object):
#    def missingNumber(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        seen = set(nums)
#
#        for i in range(len(nums) + 1):
#            if i not in seen:
#                return i
        