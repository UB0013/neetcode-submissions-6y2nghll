"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Note: None of the pointers in the new list should point to nodes in the original list.
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copymap = {None:None}
        curr= head
        while curr : 
            copymap[curr] = Node(curr.val)
            curr = curr.next 
        curr = head

        #now we have a map of our original nodes and 
        #their corresponding INDEPENDENT NODES  
        # We just need to attach these independt nodes to each other
        #basis the original node 

        # retrieving the independent nodes
        #attaching its next node  - use map ALWAYS 

        while curr :
            # we retrieve the independent nodes using the key 
            copymap[curr].next = copymap[curr.next]
            copymap[curr].random = copymap[curr.random]
            curr = curr.next
        return copymap[head]



        