'''
start with 0, then n - 1, then 1 and so forth
but i don't know length of linked list, nor can i access the last node without traversing the entire linked list
can i store the Listnode somewhere first?
e.g. res = [0, None, 1, None, ...]
when i reach the end of the linked list, populate index 1 of res
but how about index 3? where do i keep the second last listnode?
i cant put in in index 3, because i don't yet know when traversing that that is the second last node..

can i traverse the linked list twice instead?
first traversal, fill in 0, 3, 5, ... of res and get length of linked list
second traversal, start from halfway of linked list, fill in the empty spots of res from the back

if odd length, start filling from n - 2 (second-last index res)
if even length, start filling from n - 1 (last index of res)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # edge case when linked list is length = 1
        if head.next == None:
            return
        # two traversal method
        curr = head
        res = [head] # initial res with first ListNode so in the while loop i can append None first, followed by next ListNode
        res_length = 1
        curr = curr.next

        while curr:
            res.append(None)
            res.append(curr)
            res_length += 1
            curr = curr.next
        
        even = False
        if res_length % 2 == 0:
            even = True
        
        # start second traversal from second half of linked list
        first_half_length = -(-res_length // 2)
        curr = head
        i = first_half_length
        while i:
            curr = curr.next
            i -= 1
        print(curr.val)

        next_i_to_fill = res_length - 2
        if even:
            res[res_length - 1] = curr
            curr = curr.next
            next_i_to_fill = res_length - 3

        while curr:
            if res[next_i_to_fill] == None: # check that slot in array is empty before populating it
                res[next_i_to_fill] = curr
            else:
                print("something went wrong")
                print(res)
            next_i_to_fill -= 2
            curr = curr.next
        print([x.val if x is not None else None for x in res])
        
        # join ListNodes in res into a singly-linked list
        res = res[:res_length]
        print([x.val if x is not None else None for x in res])
        for i in range(len(res)):
            if i == len(res) - 1:
                res[i].next = None
                break
            res[i].next = res[i+1]
