# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        res = ListNode()
        dummy = res
        while l1 or l2 or carry:  
            addition = (l1.val if l1 else 0)  + (l2.val if l2 else 0) + carry
            
             
            l1 = l1.next  if l1 else None 
            l2= l2.next if l2 else None 
            
            res.next = ListNode(addition%10)
            carry = (addition//10)
            res = res.next
        return dummy.next
        



        