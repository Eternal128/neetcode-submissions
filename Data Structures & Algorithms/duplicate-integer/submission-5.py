class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set()

        for current_number in nums:
            if current_number in seen_numbers:
                return True
        
            seen_numbers.add(current_number)
        
        return False
        




# nums = [1, 2, 3, 1]
# true

# edge cases: an empty array -> return false



