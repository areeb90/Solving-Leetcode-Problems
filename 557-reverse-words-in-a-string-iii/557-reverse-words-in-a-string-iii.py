class Solution:
    def reverseWords(self, s: str) -> str:
         # step1: split the string
        #   split() = ["Let's","take","LeetCode","contest"]
        # step2: reverse the list 
        #   s.split()[::-1] = ["contest","LeetCode","take","Let's"]
        # step3: convert each element to string separated by space
        #   ' '.join(s.split()[::-1]) = "contest LeetCode take Let's"
        # step4: reverse the string 
        #   ' '.join(s.split()[::-1])[::-1] = "s'teL ekat edoCteeL tsetnoc"
        
        
        split = s.split()
        rev_split = split[::-1]
        return " ".join(rev_split)[::-1]