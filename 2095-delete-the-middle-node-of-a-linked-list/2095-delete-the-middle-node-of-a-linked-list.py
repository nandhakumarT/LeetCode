# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(-1,head)
        slow=fast=head
        
        #edge case
        if head is None or not head.next:
            return
            
        #slow-1,fast-2 steps in list & find the middle when right is null and left is middle
        while(fast and fast.next):
            dummy=slow
            slow=slow.next
            fast=fast.next.next
            
        dummy.next=slow.next
        return head