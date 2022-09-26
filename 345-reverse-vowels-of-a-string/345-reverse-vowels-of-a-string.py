class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=['a','e','i','o','u','A','E','I','O','U']
        res = ""
        stack=[]
        
        for char in s:
            if char in vowel:
                stack.append(char)
            
        for char in s:
            if char in vowel:
                res += stack.pop()
            else:
                res += char
        return res
        
        
        
        
        
        
        
        
        
#         v = ['a', 'e', 'i', 'o', 'u']
#         l, r = 0, len(s)-1
#         while l<r:
#             if s[l] in v:
#                 if s[r] in v:
#                     s[l], s[r] = s[r] , s[l]
#                 else:
#                     r -=1
                    
#             else:
#                 l+=1