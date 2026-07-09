class queues:
    def __init__(self):
        self.items = []   
    def enqueue(self, element):
        self.items.append(element)
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            return "Queue is empty"
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]    
    def is_empty(self):
        return len(self.items)  == 0
    def size(self):
        if not self.is_empty():
            return len(self.items)   
        return 0   
    
q = queues()
q.enqueue(1)    
q.enqueue(2)  
q.enqueue(3)  
q.enqueue(4)  
print(q.items)
print("popped element:", q.dequeue())
print("popped element:", q.dequeue())
print("popped element:", q.dequeue())
print("popped element:", q.dequeue())
print(q.items)
print("Frant element :", q.peek())
print("Is queue empty?", q.is_empty())
print("size of queue:", q.size())