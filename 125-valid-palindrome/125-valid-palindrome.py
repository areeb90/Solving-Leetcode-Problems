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
    
    
    
#             l , r = 0 , len(s)-1                    
#         while l<r:
#             while l<r and not s[l].isalnum():
#                 l +=1
#             while l<r and not s[r].isalnum():
#                 r -=1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l+=1
#             r-=1
#         return True

# ___________________________________________________________________

    
        # s=[i for i in s.lower() if i.isalnum()]
        # return s == s[::-1]
        # __________________________________________
        
#         stringg = s.replace(" ","")
#         revString = stringg[::-1]
#         if stringg == revString:
            
#             return True
#         else:
#             return False
        
                