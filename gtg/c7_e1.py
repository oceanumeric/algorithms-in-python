class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""
    
    class _Node:
        """A nonpublic class for storing a singly linked node"""
        __slots__ = "_element", "_next"
        
        def __init__(self, element, next):
            self._element = element
            self._next = next 
            
    def __init__(self):
        self._head = None
        self._tail = None 
        self._size = 0 
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0 
    
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1 
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._head._element
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1 
        
        
class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage"""
    
    class _Node:
        """A nonpublic class for storing a singly linked node"""
        __slots__ = "_element", "_next"
        
        def __init__(self, element, next):
            self._element = element
            self._next = next 
            
    def __init__(self):
        self._head = None
        self._size = 0 
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._element 
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
        
if __name__ == "__main__":
    S = LinkedStack()
    S.push(2)
    print(S._size)
    S.push(5)
    print(S._size)
    print(len(S))