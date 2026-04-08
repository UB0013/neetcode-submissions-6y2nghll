# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0 :
            return None

        while len(lists) > 1 :
            merged = [] 
            for i in range(0,len(lists),2): 
                merged.append( self.merge2 (lists[i], lists[i+1] if (i+1) < len(lists) else None )) 
            lists = merged 
        return lists [0]

    def merge2 (self, l1, l2): 
        dummy =  ListNode(0)
        curr = dummy 
        while l1 and l2  :
            if l1.val <= l2.val : 
                dummy.next = l1
                l1 = l1.next 
                dummy = dummy.next
            else : 
                dummy.next =l2
                l2 = l2.next
                dummy = dummy.next
            
        if l1 :
            dummy.next = l1 
        if l2 : 
            dummy .next =l2 

        return curr.next 
            

                 


        





        