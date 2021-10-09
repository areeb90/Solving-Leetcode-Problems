class Solution:
    def addDigits(self, num: int) -> int:
        def ad(num):
            result = 0
            while num>0:
                r = num%10
                result = result + r
                num = num//10
            return result
        
        seen = set()
        num1= 0
        while ad(num) not in seen:
            num1 = ad(num)
            if num1>=0 and num1<10:
                return num1
            else:
                seen.add(num1)
                num = num1
            