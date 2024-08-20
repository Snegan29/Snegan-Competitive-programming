# How many numbers are smaller than the current number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        List = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if(j != i and nums[j] < nums[i]):
                    count = count + 1
            List.append(count)
        return List
    

# Kids with the greatest number of candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        e = extraCandies
        s = max(candies)
        arr = []

        for i in range(n):
            if (candies[i]+e) >= s:
                arr.append(True)
            else:
                arr.append(False)
        return arr
    

# Running sum of 1d array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        d = []
        for i in range(len(nums)):
            s+=nums[i]
            d.append(s)
        return d
    

# Shuffle string
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = ""
        for i in range(len(s)):
            a = a + s[indices.index(i)]
        return a

        
# Check if two strings are equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = "".join(word1)
        b = "".join(word2)
        if a==b:
            return True
        return False
        