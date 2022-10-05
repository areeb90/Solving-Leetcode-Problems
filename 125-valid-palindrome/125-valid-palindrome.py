import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res+=i
            
        
        res = res.upper()
        print(res)
        start = 0
        end=len(res)-1
        while start <= end:
            if res[start] == res[end]:
                start+=1
                end-=1
            elif res[start] != res[end]:
                    return False
            
        return True