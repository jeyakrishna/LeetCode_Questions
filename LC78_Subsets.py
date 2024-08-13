class Solution:
    def subsets(self, nums):
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return 

            # don't pick nums[i]
            backtrack(i + 1)

            # pick nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            
        backtrack(0)
        return res

s = Solution()
print(s.subsets([1, 2, 3]))