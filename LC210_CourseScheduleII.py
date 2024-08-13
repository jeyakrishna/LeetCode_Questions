from typing import Optional
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int, int]]) -> list[int]:
        res = []
        preMap = {i : [] for i in range(numCourses)}
        counter = [0 for i in range(numCourses)]

        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            counter[crs] += 1
        
        queue = collections.deque()

        for i in range(numCourses):
            if counter[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for nei in preMap[curr]:
                counter[nei] -= 1
                if counter[nei] == 0:
                    queue.append(nei)
        
        return res if len(res) == numCourses else []

s = Solution()
print(s.findOrder(2, [[1,0]]))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(1, []))
