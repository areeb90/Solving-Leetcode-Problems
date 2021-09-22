class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        # for primary diagonal
        for i in range(len(mat)):
            res = res + mat[i][i]
            
        j = len(mat[0])-1
        

        for i in range(len(mat)):
            res = res + mat[i][j]
            j = j- 1
        
        if len(mat)%2 !=0:
            res = res - mat[len(mat)//2][len(mat)//2]
        return res