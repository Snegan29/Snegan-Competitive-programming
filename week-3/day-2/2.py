# Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        return str(int(num1)+int(num2))
        

# Find All Numbers Disappeared in an Array
class Solution(object):
    def findDisappearedNumbers(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=[]
        c=set(nums)
        for i in range(1,len(nums)+1):
            if i not in c:
                k.append(i)
        return k
    

# Perfect Number
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        ans = 1
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:
                ans += i + num // i
        return ans == num
    

# Fibonacci Number  
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2) 
    

# Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        s=''
        for i in l:
            s=s+' '+i[::-1]
        return(s[1:])
        
       