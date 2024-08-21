from typing import Optional

class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        smallest = arrays[0][0]
        largest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(largest - arr[0]))
            smallest = min(smallest, arr[0])
            largest = max(largest, arr[-1])
        
        return max_distance
        
s = Solution()
print(s.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
print(s.maxDistance([[1], [1]]))