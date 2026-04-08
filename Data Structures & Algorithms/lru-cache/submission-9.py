class Node: 
    def __init__(self, key, val ):
        self.next = None
        self.prev = None 
        self.val = val 
        self.key = key 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.left = Node (0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left 

    def get(self, key: int) -> int:
        if key in self.cache :
            self.remove (self.cache[key])
            self.insert (self.cache[key])
            return self.cache[key].val
        else :
            return -1 
    def remove (self,node) : 
        prev = node.prev
        nexx = node.next 
        prev.next = nexx
        nexx.prev = prev
    def insert (self,node) :
        temp = self.right.prev
        self.right.prev = node 
        node.next =self.right
        node.prev = temp 
        temp.next = node
  
    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            node = self.cache[key] 
            self.remove (self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])


        if len(self.cache)  > self.capacity :
            lru = self.left.next 
            self.remove (lru)
            del self.cache [lru.key]







        
