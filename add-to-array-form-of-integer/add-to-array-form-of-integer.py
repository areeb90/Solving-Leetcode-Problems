class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1 = ""
        res = []
        for i in num:
            num1 += str(i)
        result = str(int(num1)+int(k))
        res[:0] = result
        return res
        