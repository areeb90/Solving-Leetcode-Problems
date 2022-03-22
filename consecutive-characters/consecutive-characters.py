class Solution:
    def maxPower(self, s: str) -> int:
        output=0
        outputA=[]
        for i in range(len(s)):
            if s[i]==s[i-1]:
                output=output+1
            else:
                output=1
            outputA.append(output)
        return max(outputA)