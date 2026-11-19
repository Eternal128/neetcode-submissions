class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
        
        for key in freq:
            if freq[key] < 2:
                return key
        
