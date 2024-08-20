# Power of four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4
        return True
    

# Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


# Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(50000):
            if i*i==num:
                return True
        else:
            return False


# Find the Difference 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if t.count(i) > s.count(i):
                return (i)
            

# Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                l.append("FizzBuzz")

            elif i%3!=0 and i%5!=0:
                l.append(str(i))
            elif i%3==0:
                l.append("Fizz")
            elif i%5==0:
                l.append("Buzz")
            
        return l
    

