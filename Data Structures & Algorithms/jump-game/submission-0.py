class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        max_reach = 0

        for i in range(len(nums)):
            # if my current index is beyond my max reach, i am going to be stuck
            if i > max_reach:
                return False
            
            # update the furthest index
            max_reach = max(max_reach, i + nums[i])

            # if my reach covers or passes the last index, return true
            if max_reach >= len(nums) - 1:
                return True
            

        return False
        
# nums = [2, 3, 1, 1, 4]
# true

# i = 0, nums[0] = 2
# max_reach = max(0, 0 + 2) = 2

# i = 1, nums[1] = 3, max_reach becomes max(2, 1 + 3) = 4. Since 4 >= 4 return True


# [1, 0, 1]

# i = 0, nums[0] = 1
# max_reach = max(0, 0 + 1) = 1

# i = 1, nums[1] = 0. max_reach = max(1, 0) = 1






# [2, 3, 1, 1, 4]

# true 

# edge cases:
# [0] 
# true

# brute force: backtracking. too slow.


# my plan:
# - max_reach = 0
# - loop from start to max_reach 
# - max_reach = max of the current value and i + nums[i]
# - if my loop i ever exceed my max_reach i am gonna be stuck so i return false
# - if my max reach becomes greater than or rqual to the last of the array, i can return true
# - O(n) time complexity and O(1) space


# def dfs(idx):
#     if idx >= len(nums) - 1:
#         return True
    
#     max_jump = nums[idx]
#     if max_jump == 0:
#         return False
    





