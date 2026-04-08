# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0 :
            return None
       
        res = []
        
        while len (lists) > 1 : 
           
            merged = []
            for l in range(0,len(lists),2):
                first = lists[l]
                if l+1 < len (lists):
                    second = lists[l+1]
                else : 
                    second = None
                merged.append(self.merge2(first,second))
            lists = merged 
        return lists[0]




    def merge2(self,first,second):
        prev = ListNode(0,0)
        dummy = prev
        while first and second :
            print (1)
            if first.val <= second.val :
                prev.next = first
                prev = prev.next 
                first = first.next 
            else :
                prev.next = second
                prev = prev.next
                second = second.next
        if first :
            prev.next = first
        if second :
            prev.next = second

        return dummy.next
                

            
            
        return None
        