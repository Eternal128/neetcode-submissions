class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for item in nums:
            seen.add(item)
        return len(nums) != len(seen)