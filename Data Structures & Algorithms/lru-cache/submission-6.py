class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val 
        self.next = None
        self.prev = None 
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}
    def remove (self, node) : 
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def insert (self,node) :
        prev = self.right.prev
        node.next = self.right 
        self.right.prev = node
        node.prev = prev
        prev.next = node
    def get(self, key: int) -> int:
        if key in self.cache :
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1 
    def put(self, key: int, value: int) -> None:
        if key in self.cache : 
            self.remove(self.cache [key])
        node = Node(key,value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache)> self.capacity :
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
