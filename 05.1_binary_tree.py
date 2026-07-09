class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rigth = None

root = node('R')
rootA = node('A')
rootB = node('B')
rootC = node('C')
rootD = node('D')
rootE = node('E')
rootF = node('F')
rootG = node('G')

root.left = rootA
root.rigth = rootB

rootA.left = rootC
rootA.rigth = rootD

rootB.left = rootE
rootB.rigth = rootF

rootF.left = rootG

print(root.left.rigth.data)
