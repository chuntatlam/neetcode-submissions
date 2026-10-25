# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        if curr1 == None:
            return curr2
        if curr2 == None:
            return curr1

        head = None # best prac to define variables used inside a block scope outside first
        if curr1.val < curr2.val:
            head = curr1
            curr1 = head.next
        else:
            head = curr2
            curr2 = head.next
        
        merged_curr = head
        while curr1 and curr2: 
            if curr1.val < curr2.val:
                merged_curr.next = curr1
                merged_curr = curr1
                curr1 = curr1.next
            else:
                merged_curr.next = curr2
                merged_curr = curr2
                curr2 = curr2.next
        
        if curr1:
            merged_curr.next = curr1
        if curr2:
            merged_curr.next = curr2

        return head
