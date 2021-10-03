class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        l = len(arr)
        while i<l:
            if arr[i]==0:
                arr.pop(-1)
                arr.insert(i , 0)
                
                i+=1
            i+=1
            
            