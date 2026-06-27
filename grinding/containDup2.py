class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        lastIndex = {}

        for i, num in enumerate(nums):

            if num in lastIndex:
                if i - lastIndex[num] <= k:
                    return True

            lastIndex[num] = i

        return False

nums = [1,2,3,1]

k = 3

sol = Solution()

print(sol.containsNearbyDuplicate(nums, k))