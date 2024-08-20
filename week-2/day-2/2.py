#  Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = 0
        for i in nums:
            if i == target:
                return nums.index(i)
            elif i < target:
                a = nums.index(i)+1
        return a
        

# Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = s.split()
        return len(d[-1])
    

#  Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:

        low = 0
        high = x
        while low < high+1:
            mid = (low + high)//2
            midsquare = mid * mid
            
            if midsquare == x:
                return mid
                break
            elif midsquare > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
    

# Remove Duplicates from sorted list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        while a and a.next:
            if a.val == a.next.val:
                a.next = a.next.next
            else:
                a = a.next
        return head
        

# Pascal’s Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        temp = rowIndex
        for i in range(1,rowIndex+1):
            rowIndex = [1]
            
            for j in range(i-1):
                rowIndex.append(triangle[i-1][j] + triangle[i-1][j+1])
            
            rowIndex.append(1)
            
            triangle.append(rowIndex)
    
        return triangle[temp]

        