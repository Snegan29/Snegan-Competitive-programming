# To Lower Case
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
        

# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        result = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                result = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result
        

# Transpose Matrix
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l = len(matrix)
        m = len(matrix[0])

        result = [[0]*l for i in range(m)]

        for i in range(m):
            for j in range(l):
                result[i][j] = matrix[j][i]
        return result
    

# Defanging an IP Address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=""
        for i in address:
            if i == ".":
                a+='['+'.'+']'
            else:
                a+=i   
        return a        
    

# Subtract the Product and Sum of Digits of an Integer  
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        a = 1

        while n > 0:
            num = n%10
            s += num
            a *= num
            n = n//10

        return a-s

        
        
        