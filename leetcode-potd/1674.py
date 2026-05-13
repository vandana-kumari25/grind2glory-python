## 1674. Minimum Moves to Make Array Complementary

# What is Complementary Array?
# An array is complementary if for all indices i, nums[i] + nums[n - 1

def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        n = len(nums)
        sum_count = Counter()
        min_arr, max_arr = [], []

        for i in range(n // 2):
            a, b = min(nums[i], nums[n - 1 - i]), max(nums[i], nums[n - 1 -i])
            sum_count[a + b] += 1
            min_arr.append(a)
            max_arr.append(b)

        min_arr.sort()
        max_arr.sort()
        min_ops = n

        for c in range(2, 2 * limit + 1):
            add_left = n // 2 - bisect_left(min_arr, c)
            add_right = bisect_left(max_arr, c - limit)
            current_ops = n // 2 + add_left + add_right - sum_count[c]
            min_ops = min(min_ops, current_ops)

        return min_ops