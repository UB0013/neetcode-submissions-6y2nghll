# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        slow = head
        fast = head

        while fast and fast.next : 
            slow = slow.next
            fast = fast.next.next 
        second = slow.next
        slow.next = None 

        curr = head 
        prev = None 

        while second :
            temp =second.next
            second.next = prev
            prev = second
            second = temp 

        second = prev

        while second  : 
            temp1 = curr.next
            temp2 = second.next 
            curr.next = second 
            second.next = temp1 
            curr = temp1
            second = temp2 
  

            
            
            
        