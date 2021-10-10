class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) <3:
            return False
        
        
        #same number can't be repeated in an arr
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
        
        
        #index of the maximun number in an arr
        max_index = arr.index(max(arr))
        
        
        
        # Max number can't be at first or last index
        if max_index == 0 or max_index == len(arr)-1:
            return False
        
        
        increases = arr[0:max_index]
        decreases = arr[max_index: ]
        
        
        
        if increases != sorted(increases):
            return False
        if decreases != sorted(decreases, reverse=True):
            return False
        
        return True