class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        ans = tmp = len(s)   #Use tmp here to store original value of len(s)
        for v in collections.Counter(s).values():
            ans -= v % 2   # if v % 2 == 1 then ans will be deducted
        if tmp != ans:
            ans += 1   # if we deducted something we will need to add back the one odd char we can handle
        return ans
    
        # count=len(s)
        # l = []
        # counter={}
        # for letter in s:
        #     if letter not in counter:
        #         counter[letter]=0
        #     counter[letter]+=1
        # for v in counter.values():
        #     if v%2 ==1:
        #         count-=1
            
                
            
            
            
        #     if count(int(split[i])) % 2 == 0:
        #         l.append(split[i])
        #     else:
        #         count +=1
        # total = len(l)+count
        # return total
                
            
        #     if (count(split[i])//2==0):
        #         count +=1
        #     else:
        #         count+=1
        # return count