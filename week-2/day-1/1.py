# TWO SUM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range (n):
            sec_number = target - nums[i]
            
            for j in range (i+1, n):
                if sec_number == nums[j]:

                    return [i,j]
                

# Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number=0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]:
                number-=roman[s[i]]
            else:
                number+=roman[s[i]]
        return number+roman[s[-1]]
    

# Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        original = x
        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        return original == reverse
    

# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        a=[]
        for i in zip(*strs):
            if len(set(i))==1:
                a.append(i[0])
            else:
                break
        return "".join(a)
    

# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = nums
        i = 0
        j = 1


        while i < len(a)-1:
            if a[i]==a[j]:
                a.pop(j)
            else:
                i=j
                j+=1
        
        