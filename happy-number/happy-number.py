class Solution:
    def isHappy(self, n: int) -> bool:
        
        
                                                # This function is squaring each digit of the given number
        def sqSum(num):
            result = 0
            while num > 0:
                r = num %10                     #this will track the last digit of number 
                result = result + r*r
                num = num // 10                 #this will assign the num* with the exclusion of last digit 
            return result                       #return the squared sum of the digits
        
        seen= set()
        sum1=0
        while sqSum(n) not in seen:             #here *n is the given number passes to the function for                                                       spillting and squaring of its digits
            
            
        
            sum1 = sqSum(n)                     #sum1 will track the squared sum
            if sum1 == 1:
                return True
            else:
                seen.add(sum1)
                n = sum1                        #*n is the given number passes to the function
                
        return False