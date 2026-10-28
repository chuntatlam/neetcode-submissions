'''
linked list
ones -> tens -> hundreds -> ...

add the ones node tgt first
if > 9, rollover
18 max
nums % 10 -> reminder in the ones space
in the tens place, need to add an additional 1 -> assign to carry over variable
update in place 

keep it going until one or both the linked list reaches None
while curr1 and curr2 -> check both not None
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        prev1, prev2 = None, None
        carry_over = 0
        while curr1 and curr2:
            temp = (curr1.val + curr2.val + carry_over) % 10
            if curr1.val + curr2.val + carry_over > 9:
                carry_over = 1
            else:
                carry_over = 0
            curr1.val = temp
            prev1 = curr1
            curr1 = curr1.next
            prev2 = curr2
            curr2 = curr2.next
        
        # either linked list could have ended first, or both ended at the same time
        if curr1 == None and curr2 != None:
            # point end of linked list 1 to remaining of linked list 2
            prev1.next = curr2
            while curr2:
                temp = (curr2.val + carry_over) % 10
                if curr2.val + carry_over > 9:
                    carry_over = 1
                else:
                    carry_over = 0
                curr2.val = temp
                prev2 = curr2
                curr2 = curr2.next
            if carry_over == 1:
                end_node = ListNode(val=1, next=None)
                prev2.next = end_node
        elif curr2 == None and curr1 != None:
            while curr1:
                temp = (curr1.val + carry_over) % 10
                if curr1.val + carry_over > 9:
                    carry_over = 1
                else:
                    carry_over = 0
                curr1.val = temp
                prev1 = curr1
                curr1 = curr1.next
            if carry_over == 1:
                end_node = ListNode(val=1, next=None)
                prev1.next = end_node
        else:
            # check if there is existing carry_over
            if carry_over == 1:
                end_node = ListNode(val=1, next=None)
                prev1.next = end_node
        
        return l1
