# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        fast = head

        while fast and fast.next:
            tail = tail.next
            fast = fast.next.next
        
        tail.next = tail.next.next
        return dummy.next
        

        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next
        
        # curr = head
        # mid = length // 2
        # for i in range(mid):
        #     tail = curr
        #     curr = curr.next
        
        # tail.next = curr.next
        # return dummy.next


""""
dummy = ListNode(0, head)
tail = dummy
curr = head


slow = 1-3-4-7
fast= 1-4-1-6

while .....
    tail = slow
    slow = slow.next
    fast = fast.next.next
tail = 4
tail.next = slow.next


Loop the Linkedlist 
    get the length of the linkedlist = 7

7 // 2 = 3
for i in range(mid):
    tail = curr
    curr = curr.next

tail = 4
curr = 7
tail.next = curr.next
return dummy.next
"""