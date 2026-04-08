# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next= None
        prev= None  

        while second : 
            
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        second = prev
        prev= None  
        while second : 
            temp1, temp2 = head.next, second.next
            head.next = second 
            second.next = temp1
            head,second = temp1, temp2 
            





