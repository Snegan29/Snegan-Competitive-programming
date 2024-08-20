# Three Divisors
class Solution:
    def isThree(self, n: int) -> bool:
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count==3:
            return True
        else:return False   


# Maximum number of words found in a sentence
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        a = 0
        for i in sentences:
            c = len(i.split())
            if(c > a):
                a = c
        return a
    

# Rings and Rods
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        for j in range(len(rings)):
            if rings[j] in '0123456789':
                i = rings[j]
                if i in rods:
                    rods[i] += rings[j - 1]
                else:
                    rods[i] = rings[j - 1]
        lst = list(rods.items())
        count = 0
        for i in range(len(lst)):
            s = lst[i][1]
            if len(set(list(s))) == 3:
                count += 1
        return count
    

# Find first palindromic string in the array
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i[0:]==i[::-1]:
                return i
        return ""
    

# Counting words with a given prefix
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l=len(pref)
        c=0
        for i in words:
            if i[:l]==pref:
                c+=1
        return c