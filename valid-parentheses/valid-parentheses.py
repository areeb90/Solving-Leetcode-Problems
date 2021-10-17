class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        for i in s:
            if i == "(" or i=="[" or i=="{":
                x.append(i)
                
            else:
                if len(x) >= 1:
                    if i == "}":
                        if x.pop() != "{":
                            return False
                    if i == "]":
                        if x.pop() != "[":
                            return False
                    if i == ")":
                        if x.pop() != "(":
                            return False
                        
                else :
                    return False
                
        if len (x) == 0:
                return True
        else :
                return False
            
            
a = Solution()
a.isValid("killer(")