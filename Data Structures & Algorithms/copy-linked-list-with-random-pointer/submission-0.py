"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldMap = {None:None}
        curr = head 
        while curr: 
            copy = Node(curr.val)
            oldMap [curr]= copy
            curr = curr.next
        
        curr = head
        while curr : 
            copy = oldMap[curr]
            copy.next = oldMap[curr.next]
            copy.random = oldMap[curr.random]
            curr = curr.next
        return oldMap[head]
        