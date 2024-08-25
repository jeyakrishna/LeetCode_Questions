from math import log10

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        logValue = log10(n) / log10(4)
        return logValue == int(logValue)