# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res=[]
        dummy=point=ListNode(0)
        
        for i in lists:
            while i:
                res.append(i.val)
                i=i.next
        for l in sorted(res):
            point.next=ListNode(l)
            point=point.next
        return dummy.next
            