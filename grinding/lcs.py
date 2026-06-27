class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:

            # Start only if num is the beginning
            if num - 1 not in numSet:

                current = num
                length = 1

                while current + 1 in numSet:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest

nums=[1,2,3,4]
sol = Solution()
print(sol.longestConsecutive(nums))