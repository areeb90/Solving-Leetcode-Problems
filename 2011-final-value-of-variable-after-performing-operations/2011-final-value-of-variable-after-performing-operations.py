class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for index in operations:
            if '-' in index:
                res -= 1

            elif '+' in index:
                res += 1
            
        return res
