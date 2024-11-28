class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                res += s[i-1]

        res += s[-1]

        return res
