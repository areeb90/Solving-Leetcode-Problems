class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,j in enumerate(s):
            if s.count(j)==1:
                return i
            
        return -1
        
        
        # arr = []
        # arr = s.split(",")
        # for i in arr:
        #     if arr.count(i)==1:
        #         return arr.index(i)
        #     else:
        #         return -1
        