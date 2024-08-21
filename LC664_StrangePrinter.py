from typing import Optional

# 1. Remove side by side duplicates
# 2. Initialize a dict for storing the values
# 3. Call dp helper function to count the min turns needed.
#   a. take the first and last occurence of the string so we can reduce the overall typing by 1
#       for ex. aba -> aaa and replace center a with b
#       or abaabbaa -> string after removing duplicates will be ababa
            # step1: aaaaa
            # step2: replace 1st index a with b -> abaaa
            # step3: replace 3rd index a with b -> ababa

class Solution:
    def strangePrinter(self, s: str) -> int:
        
        def removeDuplicates(s: str) -> str:
            new_string = ''
            for i in range(len(s)):
                if len(new_string) == 0:
                    new_string += s[i]
                else:
                    if new_string[-1] != s[i]:
                        new_string += s[i]
            
            return new_string
        
        # Remove side by side duplicates 
        s = removeDuplicates(s)
        memo = {}

        def helper(start: int, end: int) -> int:
            # Base Condition
            if start > end:
                return 0

            # if res in memo
            if (start, end) in memo:
                return memo[(start, end)]
            
            # Worst Case Scenario (printing each one at a type and moving forward)
            min_turns = 1 + helper(start + 1, end)

            # Optimal Scenario (finding for the same character in the string)
            for k in range(start + 1, end + 1):
                if s[start] == s[k]:
                    turns_with_match = helper(start, k - 1) + helper(k + 1, end)
                    min_turns = min(min_turns, turns_with_match)

            # memoize the result
            memo[(start, end)] = min_turns
            return min_turns
        
        return helper(0, len(s) - 1)

s = Solution()
print(s.strangePrinter("aaabbb"))
print(s.strangePrinter('aba'))
print(s.strangePrinter('bcbccaaba'))