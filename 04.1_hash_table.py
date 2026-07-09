world = [[],[],[],[],[],[],[],[],[],[]]
   
def chracte_no(value):
    sum_of_chracter = 0
    for char in value:
        sum_of_chracter += ord(char)
    return sum_of_chracter%10
def add(name):
    index = chracte_no(name)
    world[index].append(name)
def contanuer(name):
    index = chracte_no(name)
    return world[index] == name    

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(world)
