# Ideas
# 1. Mirror the first half and create the reverse of it
# 2. Increment the first half by 1 and mirror it
# 3. Decrement the first half by 1 and mirror it
# 4. Edge Cases -> Add the form 9999
# 5. Edge Cases -> Add the form 100..001

class Solution:
    def half_to_palindrome(self, left: int, even: bool) -> int:
        res = left
        
        if not even:
            left = left // 10
        while left:
            res = res * 10 + left % 10
            left = left // 10
        
        return res

    def nearestPalindrome(self, n: str) -> str:
        len_n = len(n)
        i = len_n // 2 - 1 if len_n % 2 == 0 else len_n // 2

        first_half = int(n[ : i + 1])

        possibilities = []
        possibilities.append(self.half_to_palindrome(first_half, len_n % 2 == 0))
        possibilities.append(self.half_to_palindrome(first_half + 1, len_n % 2 == 0))
        possibilities.append(self.half_to_palindrome(first_half - 1, len_n % 2 == 0))
        possibilities.append(10 ** (len_n - 1) - 1)
        possibilities.append(10 ** len_n + 1)

        diff = float("inf")
        res = 0
        nl = int(n)

        for cand in possibilities:
            if cand == nl:
                continue
            if abs(cand - nl) < diff:
                diff = abs(cand - nl)
                res = cand
            elif abs(cand - nl) == diff:
                res = min(diff, cand)
        
        return str(res)


s = Solution()
print(s.nearestPalindrome("123"))
print(s.nearestPalindrome("1"))