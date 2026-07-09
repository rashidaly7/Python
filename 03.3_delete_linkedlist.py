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

def delete(node, deleted_node):
    if node == deleted_node:
        return node.next
    current_node = node
    while current_node.next and current_node.next != deleted_node:
        current_node = current_node.next
    if current_node is None:
        return node
    a = current_node.next
    current_node.next = a.next
    return node


node1 = node(65)
node2 = node(23)
node3 = node(12)
node4 = node(76)

node1.next = node2
node2.next = node3
node3.next = node4
display(node1)

node1 = delete(node1, node3)
display(node1)




    