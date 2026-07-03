class Solution(object):
    def isPalindrome(self, x):

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse_half = 0

        while x > reverse_half:

            reverse_half = reverse_half * 10 + x % 10
            x //= 10

        return x == reverse_half or x == reverse_half // 10

x = 12321
sol = Solution()
print(sol.isPalindrome(x))

# Complexity
# Time: O(n)
# Space: O(1)












class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
        

# Complexity
# Time: O(n)
# Space: O(n) (because of str(x))
# Interview Note

# For LeetCode, this is perfectly acceptable unless the problem explicitly forbids converting the integer to a string.

# In interviews, however, after presenting this solution, you can say:

# "This solution is simple and readable. If string conversion is not allowed, I can solve it using integer manipulation by reversing half of the number, which uses O(1) extra space."