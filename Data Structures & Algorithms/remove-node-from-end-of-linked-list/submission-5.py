# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0,head)
        tail = dummy 
        

        while n >0 :
            curr = curr.next
            n -= 1 
        
        while curr :
            dummy = dummy.next
            curr = curr.next

        dummy.next = dummy.next.next

        return tail.next

        