class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        
        def helper(start, path, total):
            if total > target:
                return 
            if total == target:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                helper(i + 1, path + [candidates[i]], total + candidates[i])
        
        helper(0, [], 0)
        return res

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([2,5,2,1,2], 5))