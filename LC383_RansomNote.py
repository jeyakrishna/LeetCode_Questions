from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        
        for s in ransomNote:
            if s in counter:
                counter[s] -= 1
                if counter[s] < 0:
                    return False
            else:
                return False

        return True