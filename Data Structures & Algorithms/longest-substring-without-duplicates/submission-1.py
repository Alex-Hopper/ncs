class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        res = 0

        for r in range(len(s)):
            c = s[r]
            if c in seen:
                l = max(l, seen[c] + 1)
            seen[c] = r

            res = max(res, r - l + 1)

        return res