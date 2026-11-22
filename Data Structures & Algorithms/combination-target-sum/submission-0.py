class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start_index, current_path, remaining_target):
            #base case: if the target is met, save the valid path
            if remaining_target == 0:
                result.append(current_path.copy())
                return
            
            for i in range(start_index, len(nums)):
                num = nums[i]

                if num > remaining_target:
                    break

                current_path.append(num)
                backtrack(i, current_path, remaining_target - num)
                current_path.pop() # remove the last numebr to try the next option

        backtrack(0, [], target)
        return result

    



# [2, 3] 
# target = 5

# [2]
# target = 3

# [2, 2]
# target = 1

# backtrack

# [2, 3]
# target = 0

# result.append([2,3])
# [2,3]





        



    # [2, 3, 6, 5]
    # 7

    # 2, 2, 3 -> 7

    # [2,2,3], [7]

    # edge cases:
    # [] -> empty
    # [] -> empty if the target is smaller than the smallest number in the list



