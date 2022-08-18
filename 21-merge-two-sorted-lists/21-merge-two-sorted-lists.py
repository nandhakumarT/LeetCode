# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #create the dummy node
        dummy=ListNode()
        res=dummy
        
        #checking if l1 first value is less than l2 first value then add the lesser value to res
        #checking if l2 first value is less than l1 first value then add the lesser value to res
        while l1 and l2:
            
            if l1.val<l2.val:
                res.next=l1
                l1=l1.next
            else:
                res.next=l2
                l2=l2.next
            res=res.next
            
        #if l2 is None and l1 is not None--> return balance value in the dummy
        if l1:
            res.next=l1
        #if l1 is None and l2 is not None--> return balance value in the dummy
        elif l2:
            res.next=l2
            
        return dummy.next
        
    
                    
                    
                    