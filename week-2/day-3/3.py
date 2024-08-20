# Best Time To Buy And Sell Stocks
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = prices[0]
        b = 0
        
        for price in prices[1:]:
            b = max(b, price - a)
            a = min(a, price)
            
        return b
    

# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = s.lower()
        d = []
        for i in range(0,len(c)):
            if c[i].isalnum():
                d.append(c[i])
        
        if d[0:] == d[::-1]:
            return True
        return False

        
# Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for ele in nums:
            if ele in s:
                s.remove(ele)
            else:
                s.add(ele)
        
        for ans in s:
            return ans
        

# Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
    

# Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        l = []
        while s != '1':
            c = 0
            for i in s:
                c += (int(i) ** 2)
            if c in l:
                return 0
            l.append(c)
            s = str(c)
        return 1