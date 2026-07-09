class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.front = None
        self.head = None
        self.size = 0 
    def push(self, element):
        new_node = node(element)
        if self.head is None:
            self.front = self.head = new_node
            return
        self.head.next = new_node
        self.head = new_node
        self.size += 1
    def peek(self):
        if self.head is None:
            return "list is empty"
        return self.head.data   
    def pop(self):
        popped = self.front
        self.front = self.front.next 
        return popped.data
    def peek(self):
        if self.front is None:
            return "list is empty"
        return self.front.data   
    def is_empty(self):
        return self.front == None
    def sizes(self):
        return self.size
    def display(self):
        current = self.front
        while current != None:
            print(current.data, end=" ->")
            current = current.next 
        
        
list = linked_list()
list.push(10)        
list.push(20)       
list.push(30)       
list.push(40)  
list.display()
print("")
print("top element is :", list.peek())
print("popped element is :", list.pop())
list.display()
print("")
print("top element is :", list.peek())
print("list is empty :", list.is_empty())
print("size of list is :", list.sizes())