class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def ways(k: int) -> int:
            if k <= 2:
                return k
            if k in memo:
                return memo[k] 
            else:
                memo[k] = ways(k-1) + ways(k-2)
            return memo[k]
        
        return ways(n)