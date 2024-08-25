class Solution:
    def fractionAddition(self, expression: str) -> str:

        def findNumeratorsAndDenominators(s: str):
            cur_num = 0 
            numerators = []
            denominators = []
            sign = True

            if expression[0] == '+':
                sign = True
            elif expression[0] == '-':
                sign = False
            else:
                cur_num = int(expression[0])    

            for i in range(1, len(expression)):
                if expression[i] == '+':
                    sign = True
                    denominators.append(cur_num)
                    cur_num = 0
                elif expression[i] == '-':
                    sign = False
                    denominators.append(cur_num)
                    cur_num = 0
                elif expression[i] == '/':
                    if sign == True:
                        numerators.append(cur_num)
                    else:
                        numerators.append(-(cur_num))
                    cur_num = 0
                else:
                    cur_num = cur_num * 10 + int(expression[i])
            
            denominators.append(cur_num)
            return numerators, denominators
        

        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        

        def lcm(a: int, b: int) -> int:
            return abs(a * b) // gcd(a, b)
        
        numerators, denominators = findNumeratorsAndDenominators(expression)

        if len(denominators) == 1:
            return expression

        cur_lcm = denominators[0]
        for denominator in denominators[1:]:
            cur_lcm = lcm(cur_lcm, denominator)
        
        numerator = 0
        
        for i in range(len(numerators)):
            multiplier = cur_lcm // denominators[i]
            numerator += (numerators[i] * multiplier)
        
        if numerator == 0:
            return "0/1"

        cur_gcd = gcd(numerator, cur_lcm)
        numerator = numerator // cur_gcd
        cur_lcm = cur_lcm // cur_gcd
        return str(numerator) + "/" + str(cur_lcm)
        
    
s = Solution()
print(s.fractionAddition("-1/2+1/2"))
print(s.fractionAddition("-1/2+1/2+1/3"))
print(s.fractionAddition("1/3-1/2"))