class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        length = len(arr)
        
        while index < length:
            if arr[index]== 0:
                arr.pop(-1)
                arr.insert(index , 0 )
                
                index +=1
                
            index +=1
            