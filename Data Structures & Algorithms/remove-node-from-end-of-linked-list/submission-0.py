'''
intuitively, i can go first pass to get length of linked list
- keeping track of length with a length_counter

second pass, find the nth element from the back, assign prev.next = prev.next.next
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # handle length = 1 edge case
        if head.next == None and n == 1:
            return None

        curr = head
        length_counter = 0 

        while curr:
            length_counter += 1
            curr = curr.next
        
        to_remove = length_counter - n

        prev, curr = None, head
        curr_index = 0

        # edge case when the first ListNode is to be removed
        if curr_index == to_remove:
            return head.next

        while curr:
            if curr_index == to_remove:
                prev.next = prev.next.next
                return head
            prev = curr
            curr = curr.next
            curr_index += 1
        
        return head


        