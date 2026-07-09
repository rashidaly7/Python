class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0 
    def push(self, element):
        new_node = node(element)   
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    def peek(self):
        if self.head is None:
            return "list is empty"
        return self.head.data   
    def pop(self):
        popped = self.head
        self.head = self.head.next 
        return popped.data
    def peek(self):
        if self.head is None:
            return "list is empty"
        return self.head.data   
    def is_empty(self):
        return self.head == 0
    def sizes(self):
        return self.size
    def display(self):
        current = self.head
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
