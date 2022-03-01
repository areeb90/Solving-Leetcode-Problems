class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        final_s=[]
        final_t=[]
#         for s
        for char in s:
            if char == '#':
                if final_s:
                    final_s.pop()
            else:
                final_s.append(char)
#         for t
        for char in t:
            if char == '#':
                if final_t:
                    final_t.pop()
            else:
                final_t.append(char)
                
        return final_s==final_t
          