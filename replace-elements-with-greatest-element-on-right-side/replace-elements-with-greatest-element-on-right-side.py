class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # index = 0
        # for i in range(1,len(arr)-1):
        #     if index < len(arr)-2:
        #         maxE = max(arr[i:])
        #         arr[index] = maxE
        #         index +=1
        # arr.append(-1)
        # return arr
        
        
        # index = 0
        # curr = arr[0]
        # for i in range(1,len(arr)-1):
        #     maxE = max(arr[index:-1])
        #     curr = maxE
        #     arr[index] = curr
        #     index +=1
        # arr.append(-1)
        # return arr
        
        
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])       # max(arr) searches for the largest number after the current index
        arr[-1] = -1
        return arr
        