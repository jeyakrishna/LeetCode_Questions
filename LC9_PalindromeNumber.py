class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        new_num = 0
        cur_num = x
        while cur_num:
            new_num = new_num * 10 + (cur_num % 10)
            cur_num = cur_num // 10
        
        return new_num == x

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))