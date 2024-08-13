class Solution:
    def recursion(self, array):
        dp = [0] * len(array)
        dp[0] = array[0]
        dp[1] = max(array[0], array[1])

        for i in range(2, len(array)):
            dp[i] = max(dp[i - 1], array[i] + dp[i - 2])
        
        return dp[-1]

    def rob(self, nums):
        n = len(nums)
        if n <= 3:
            return max(nums)
            
        a = self.recursion(nums[1:])
        b = self.recursion(nums[:-1])

        return max(a, b)

s = Solution()
print(s.rob([2, 3, 2]))
print(s.rob([1, 2, 3, 1]))
print(s.rob([1, 2, 3]))