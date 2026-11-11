class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        best = 0
        for right in range(0, len(s)):
            while s[right] in charSet: # O(1)
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            right += 1
            best = max(best, right - left)
        return best










        