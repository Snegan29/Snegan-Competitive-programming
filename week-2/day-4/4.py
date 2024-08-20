# Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        seen = set()
        for i, j in zip(s, t):
            if i in d:
                if d[i] != j:
                    return False
            else:
                if j in seen:
                    return False
                seen.add(j)
                d[i] = j
        return True
    

# Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while  current is not None:
            next = current.next 
            current.next = previous
            previous = current
            current = next 
        return previous

        
# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0,32):
            s = 2**i
            if s==n:
                return True
                break
        return False
    
# Delete Node in a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next

        
        