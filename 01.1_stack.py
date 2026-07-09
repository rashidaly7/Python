class List:
    def __init__(self):
        self.list = []
        
    def pus(self, element):
        self.list.append(element)    
        
    def popp(self):
        if len(self.list) == 0:
            return "list is empty" 
        self.list.pop()
          
    def peek(self):
        if len(self.list) == 0:
           return "list is empty" 
        return self.list[-1]   
        
    def length(self):
        if len(self.list) == 0:
           return "list is empty" 
        return len(self.list)   
        
mylist = List()        
mylist.pus("A")
mylist.pus("B")
mylist.pus("C")
mylist.pus("D")

print(mylist.list)
mylist.popp()
print(mylist.list)
print(mylist.peek())
print(mylist.length())

