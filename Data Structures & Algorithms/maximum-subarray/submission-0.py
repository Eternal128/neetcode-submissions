class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            # take the max between the current number or extending
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

        return max_sum
            





# [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# [-2, 1, 3]

# [1, 3], [-2, 1]


# current_sum and max_sum 


# edge cases:
# if not num:
#     return 0

# current_sum = nums[0]
# max_sum = nums[0]

# for num in nums[1:]:
#     # take the max between the current number or extending
#     current_sum = max(current_sum + num, max_sum)
#     max_sum = max(max_sum, current_sum)

# return max_sum







