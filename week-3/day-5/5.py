# Goal Parser Interpretation
class Solution:
    def interpret(self, command: str) -> str:
        if "()" or "(al)" in command:
            a = command.replace("()","o").replace("(al)","al")
            return a
        return command
        
        
# Count of matches in Tournament
class Solution:
    def numberOfMatches(self, n: int) -> int:
        c = 0
        while n!=1:
            c+=n//2
            n-=n//2
        return c
    

# Truncate Sentence
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        b = s.split()

        for i in b:
            a = " ".join(b[:k])
        return a
    

# Sign of the Product of the array
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1

        for num in nums:
            if num < 0:
                sign *= -1
            if num == 0:
                return 0

        return sign


# Concatenation of array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = nums
        return a+a
        