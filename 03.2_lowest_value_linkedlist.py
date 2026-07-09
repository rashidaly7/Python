class node:
    def __init__(self, data):
        self.data = data
        self.next = None   
    
def lowest_value(node):
    min = node
    minvale = min.data
    while min != None:
        if min.data < minvale:
            minvale = min.data
        min = min.next   
    print("Lowest value in linked list is :", minvale)        
    
node1 = node(65)
node2 = node(23)
node3 = node(12)
node4 = node(76)

node1.next = node2
node2.next = node3
node3.next = node4

lowest_value(node1)
    