class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x= 0
        # dont actually need to create the nums variable as just the output number is required!
		#creates a variable to store the output, i have gave it the default value of 0, because 0 is immune to XOR operation.
        for i in range(n):
#             calculating XOR operations directly
            x = x^(start+2*i) 
        return x
    
    
    
