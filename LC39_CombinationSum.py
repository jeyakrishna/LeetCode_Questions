class Solution:
    def combinationSum(self, candidates, target):
        n = len(candidates)
        res = []
        def backtrack(index, comb, total):
            if total == target:
                res.append(comb[:])
                return
            
            if total > target or index == n:
                return

            comb.append(candidates[index])
            backtrack(index, comb, total + candidates[index])
            comb.pop()
            backtrack(index + 1, comb, total)

            return res

            # for i in range(index, n):
            #     # backtrack(index + 1, total)
            #     sol.append(candidates[i])
            #     backtrack(i, total + candidates[i])
            #     sol.pop()
        
        return backtrack(0, [], 0)

s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))


