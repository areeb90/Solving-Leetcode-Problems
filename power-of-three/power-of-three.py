class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 1
        i = 0
        while (num<=n):
            num = 3**i
            i+=1
            if (num == n):
                return True
            
        return False