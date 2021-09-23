class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        # for primary diagonal
        for i in range(len(mat)):
            res = res + mat[i][i]
        
        
        
        
        #For secondary diagonal
        j = len(mat[0])-1
        
        
        for i in range(len(mat)):
            res = res + mat[i][j]
            j = j- 1
        
        
#         since the element which is common in both diagonals, is counted only once. so we subtract that element from the total result 
        if len(mat)%2 !=0:
            res = res - mat[len(mat)//2][len(mat)//2]
        return res
