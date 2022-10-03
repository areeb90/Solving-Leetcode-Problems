class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)                      #count the # of letters in a string
        count=0
        singular_or_oddLetter=0
        for v in c:      
            
            if c[v]%2 ==0:                  #check if divisible by 2 add the # of objects with the count
               count += c[v]
            elif c[v]%2 == 1 :             #if odd, then do -1 make it even to get add in count
                count += c[v]-1
                singular_or_oddLetter=1
        if singular_or_oddLetter == 1:  #items having value==1 will add 1 to the total count
            count+=1
        return count
        
        
        
        
        
        
        
        
        
        
#         ans = tmp = len(s)                            #Use tmp here to store original value of len(s)
#         for v in collections.Counter(s).values():
#             ans -= v % 2                              # if v % 2 == 1 then ans will be deducted
#         if tmp != ans:
#             ans += 1                                  # if we deducted something we will need to add back the one odd char we can handle
#         return ans
    