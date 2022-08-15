# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Step 1
        slow = fast = head
		
		#Step 2
        while(n>0):
            fast = fast.next
            n-=1
			
		#Step 3
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next
			
		#Step 4
        if(fast):
            slow.next = slow.next.next
        else:
            head = head.next
        return head
    
    
      # h=(len(head))-1
        #if head==[]:
            #return
        
       # for i in range(h,-1,-1):
        #    if n<=len(head)-1:
         #       l=n-1
          #      head.remove(l)
           # res=head[::-1]
       # return res
            
                