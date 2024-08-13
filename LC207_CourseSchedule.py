from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        counter = [0] * numCourses
        mapping = defaultdict(list)
        queue = deque()
        count = 0

        for crs, pre in prerequisites:
            counter[crs] += 1
            mapping[pre].append(crs)
        
        for i in range(numCourses):
            if counter[i] == 0:
                count += 1
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for nei in mapping[node]:
                counter[nei] -= 1
                if counter[nei] == 0:
                    count += 1
                    queue.append(nei)

        return count == numCourses


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))