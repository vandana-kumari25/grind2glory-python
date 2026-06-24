class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_items = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [item[0] for item in sorted_items[:k]]

nums = [1,1,1,2,2,3,3,3,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))