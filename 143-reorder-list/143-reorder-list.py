# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head is None:
            return None
        
        slow,fast=head,head.next
        #two half
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
        
        
        
        #reverse the second half
        second=slow.next
        prev=slow.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
            
        
        
        #merge the both half
        first,second=head,prev
        
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
            
            
        
        
        
        