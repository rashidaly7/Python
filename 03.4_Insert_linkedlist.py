class node:
    def __init__(self, data):
        self.data = data
        self.next = None
def display(node):
    current_node = node
    while current_node != None:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
def insert(n, add_node, node):
    if n==1:
        add_node.next = node
        return add_node
    i = 1
    current_node = node
    while i < n-1:
        current_node = current_node.next
        i +=1 
    if current_node ==None:
        return "out of range"    
    a = current_node.next
    current_node.next = add_node
    add_node.next = a

    return node
    

    
node1 = node(10)
node2 = node(20)
node4 = node(40)

node1.next = node2
node2.next = node4

display(node1)

add_node = node(30)
node1 = insert(3, add_node, node1)
print("")
display(node1)