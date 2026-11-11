class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: #empty string
            return 0
        
        char_count = {} # hash map
        left = 0
        max_frequency = 0
        max_length = 0

        # Expand the right with the right pointer
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            max_frequency = max(max_frequency, char_count[s[right]]) #track the maximum frequncy of a single character

            #if replacements are needed
            if (right - left + 1) - max_frequency > k:
                char_count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length




