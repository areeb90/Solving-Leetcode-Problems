class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        num = n
        res = []
        valid_pow=[]
        while n>0:
            res.append(int(n%3))
            n =int( n/3)
        for i in range(len(res)):
            if res[i]==1:
                    valid_pow.append(3**i)
        if sum(valid_pow) == num:
            return True
        else:
            return False