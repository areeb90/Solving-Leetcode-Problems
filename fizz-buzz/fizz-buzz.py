class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1 , n+1):
            if (i%3 == 0 and i%5==0):
                l.insert(i-1 , "FizzBuzz")
            elif (i%3 == 0):
                l.insert(i-1, "Fizz")
            elif (i%5==0):
                l.insert(i-1 , "Buzz")
            else:
                l.insert(i-1,  str(i))
        return l