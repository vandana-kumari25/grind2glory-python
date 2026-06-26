class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(pattern)):

            c = pattern[i]
            w = words[i]

            if c in map1 and map1[c] != w:
                return False

            if w in map2 and map2[w] != c:
                return False

            map1[c] = w
            map2[w] = c

        return True

pattern = "abcd"

s = "dog cat pay book"

sol = Solution()
print(sol.wordPattern(pattern,s))