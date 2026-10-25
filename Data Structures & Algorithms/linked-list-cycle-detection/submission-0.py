'''
at each visited ListNode, add it to a set
ListNode is hashable, can be used as an item in set
if ListNode.next points to a visited ListNode, i.e. check .next whether is in the set -> returns True
if ListNode.next points to None, return False
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        s = set()
        while curr != None:
            s.add(curr)
            if curr.next in s:
                return True
            curr = curr.next
        return False
