class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        arr.append((s[:spaces[0]]))
        for index in range(1, len(spaces)):
            arr.append(s[spaces[index-1]: spaces[index]])
        arr.append(s[spaces[-1]:])
        return ' '.join(arr)
