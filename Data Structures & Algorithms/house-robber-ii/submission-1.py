class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) < 2:
            return nums[0]

        def rob_linear(m: List[int]) -> int:
            n = len(m)
            dp = [0] * (n)
            dp[0] = m[0]
            if n > 1:
                dp[1] = max(m[0], m[1])
            for i in range(2, n):
                dp[i] = max(m[i] + dp[i-2], dp[i-1])
            return dp[n-1]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))







