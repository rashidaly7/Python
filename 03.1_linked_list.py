class node:
    def __init__(self, data):
        self.data = data
        self.next = None
def display(node):
    current = node
    while current != None:
        print(current.data, end=" -> ")
        current = current.next 
    print("Null")    

node1 = node(10)
node2 = node(20)
node3 = node(20)
node4 = node(20)

node1.next = node2
node2.next = node3
node3.next = node4

display(node1)
