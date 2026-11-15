class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        freq1 = {}
        freq_window = {}

        for i, letter in enumerate(s1):
            freq1[letter] = freq1.get(letter,0) + 1
        

        for right, letter in enumerate(s2):
            freq_window[letter] = freq_window.get(letter, 0) + 1
            while right - left + 1 > len(s1):
                freq_window[s2[left]] -= 1
                if freq_window[s2[left]] == 0:
                    freq_window.pop(s2[left], None)
                left += 1

            if freq_window == freq1:
                return True
    

        return False