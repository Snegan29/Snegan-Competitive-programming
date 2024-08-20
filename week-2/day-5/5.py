# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        return False
    
# Add Digits
class Solution:
   def addDigits(self, num: int) -> int:
				while num > 9:
					sum = 0
					while num:
						sum += num%10
						num = num//10
					num = sum

				return num
   

# Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        n = len(nums)

        for i in range(n):
            if(nums[i] != 0 ):
                nums[c],nums[i] = nums[i],nums[c]
                c+=1
            
        
# Nim Game
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        

# Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if( n <=0): 
            return False
        x = 1
        while (x<n):  
            x *=3
        return x==n
        