# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:



        dummy = ListNode(None,head)
        count = 0 
        curr = dummy
        count = 0 
        lc = dummy 


        while left > 0 : 
            lc = curr
            curr = curr.next
            left = left -1 
        print (lc.val)

        curr = dummy 

        while right >= 0 :
            rc = curr
            curr = curr.next
            right = right-1
        if not rc:
            return 

    




        def reverse (lc, rc) :
            lastnode = lc.next
            lc.next = None 
            groupnxt = rc.next 
            rc.next = None 
            
            curr = lastnode
            prev= lc
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            lastnode.next = groupnxt 
            lc.next = prev  
        reverse(lc,rc)
        return dummy.next









            

            


            






        
        