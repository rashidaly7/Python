import numpy as np
# x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# x1 = x.reshape(4,3)
# print(x1)

# arr = np.array([3,4,2,6,1,8,2,3,0,9,8,])
# print(np.sort(arr))

# y = np.array([3, 43, 12, 6, 29])
# x = np.array([True, False, True, False, True])
# newarry = y[x]
# print(newarry)

# from numpy import random
# x = random.randint(100) # zero dimension array
# x = random.randint(100, size=(5)) # one dimension array
# x = random.randint(100, size=(x, y)) # two dimension array
# x = random.randint(100, size=(x, y, z)) # tree dimension array
# print(type(x))
# print(x)

# x = random.rand(10) #one dimension array
# x = random.rand(10, 5) #two dimension array
# print(x)

# x = random.choice([3, 5, 7, 9]) # zero dimension array
# x = random.choice([3, 5, 7, 9], size=(3)) # one dimension array
# x = random.choice([3, 5, 7, 9], size=(3, 4)) # two dimension array
# print(x) 

# we can cantrol the probality by using p parameter
# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.5, 0.1], size=(10)) # one dimension array   
# print(x)

# arr = np.array([1,2,3,4,5])
# random.shuffle(arr) # the shuffle method chandes to origing array
# print(arr)
# print(random.permutation(arr)) # the permutation method retun a new array, original array not chang

# python matplotib

#numpy unfuc
# thia is a funtion type 
# x = [1,2,3,4,5]
# y = [6,7,8,9,1]         
# z = np.add(x, y)
# z = np.subtract(x, y)
# z = np.divide(x, y)
# z = np.multiply(x, y)
# z = np.absolute(x, y) #output: |x1|, |x2|.....
# z = np.fix(x, y) # output: [1.234, -2.5355] -> [1, -2]
# z = np.around(x, y) # output: (3.16666, 2) -> 3.17
# z = np.fix(x, y) # output: [3.166, -3.666] -> [3, -4]
# print(z)

#numpy log (nature log xbas log)
# arr = np.arange(1,10)
# # x = np.log2(arr)
# # x = np.log10(arr)
# x = np.log(arr) # this is nature log
# print(x)

# x = np.array([1,2,3,4])
# y = np.array([1,2,3,4])
# z = np.sum([x,y])
# z = np.prod([x,y]) #or
# z = np.prod(x) # this is single line prod
# z = np.sum([x,y], axis=1)
# z = np.prod([x,y], axis=1)
# z = np.diff(x)
# print(z)

# x = np.array([1,1,3,4,2,1,2,3,4])
# a = np.unique(x)
# print(a)