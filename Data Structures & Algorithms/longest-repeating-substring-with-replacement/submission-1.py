class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        max_length = 0
        max_freq = 0
        freq = {} #hash map to count occurences
        left = 0


        for right, letter in enumerate(s):
            freq[letter] = freq.get(letter, 0) + 1
            max_freq = max(max_freq, freq[letter]) #track max freq of a single character

            if (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

