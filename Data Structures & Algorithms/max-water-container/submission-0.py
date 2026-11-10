class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0

# RULE: smallest side of the pointer is the one that moves

        left, right = 0, len(heights)-1

        while left < right:
            curr_area = (right - left) * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            if curr_area > area:
                area = curr_area
        return area
        



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36

# 1 7 2 5 4 7 3 6
# farthest apart and the minimum value of both values become the height.

# left, right = L, R

# 1 7 2 5 4 7 3 6
# L             R

# base = (right - left)

# 1 7 2 5 4 7 3 6
# L             R

# height = min(heights[left], heights[right])


# 1 7 2 5 4 7 3 6
#   L           R


# 1 7 2 5 4 7 3 6
#   L         R

# 1 7 2 10000 1000001 7 3 6
#   L                 R

# 1 7 2 10000 1000001 7 3 6
#     L          R


# 1 7 2 10000 1000001 7 3 6
#         L      R


