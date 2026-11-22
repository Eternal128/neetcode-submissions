class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result_list = [] #list to hold all the valid subsets

        def build_subsets(start_index: int, current_path: List[int]):
            result_list.append(current_path.copy())

            for i in range(start_index, len(nums)):
                current_path.append(nums[i]) # choose the number by adding it to the path
                build_subsets(i+1, current_path) 
                current_path.pop() # unchoose the number by popping it off
                    
        build_subsets(0, [])
        return result_list


