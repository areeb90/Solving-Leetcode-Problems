class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0
        for i in range(len(arr)):
            if arr[i]%2 == 0:
                c=0 
            else:
                c +=1
            
            if c == 3:
                return True
        
        
        
        
        
        # for i in range(len(arr)):
        #     if arr[i]%2 ==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
        #         return True
        #     else :
        #         return False

        