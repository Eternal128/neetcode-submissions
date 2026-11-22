import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initliaze the class with k and the initial numbers
            self.k = k
            self.heap = []

            # add each number in our min-heap
            for num in nums:
                self.add(num)

    # add a new value and return the kth largest element
    def add(self, val: int) -> int:
        # push the value on the heap
        heapq.heappush(self.heap, val)

        
        # if we have more than k elements, we want to remove the smallest one
        # because it is guranteed that there are k element to make the operation
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # root of the min-heap is gonna be our kth largest element
        return self.heap[0]






        

# k = 3
# nums = [4, 5, 8, 2]

# [2, 4, 5, 8]
# 4

# [2, 3, 4, 5, 8]
# 4

# [2, 3, 4, 5, 5, 8]
# 5


# use a min-heap

# 


