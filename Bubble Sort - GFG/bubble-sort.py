#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for num in range (len(arr)):
            for i in range(0, len(arr)-1):
                if arr[i+1] < arr[i]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                    
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends