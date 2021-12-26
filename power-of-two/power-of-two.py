class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        i=0
        while (num <= n):
            num = 2**i
            
            if (num == n):
                return True
            i+=1
        
        return False