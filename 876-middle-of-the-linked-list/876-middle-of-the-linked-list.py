# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast=slow=head
        
        if head is None:
            return head
        
        while fast and fast.next:
                    
            slow=slow.next
            fast=fast.next.next
                
        return slow
                
"""
        public:
    ListNode* middleNode(ListNode* head) 
    {
        ListNode *slow = head;
        ListNode *fast = head;
        
        while(fast != NULL and fast -> next != NULL)
        {
            slow = slow -> next;
            fast = fast -> next -> next;
        }
        return slow;
    }
};
"""         
        