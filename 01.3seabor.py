

# sns.displot([0,1,2,3,4,5])
# sns.displot([0,1,2,3,4,5], kind="kde")
# plt.show()

# normal distributon

# x = random.normal(size=(2,3))
# print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#viscalization os norm distribution
# data = random.normal(size=100)
# sns.displot(data, kind="kde")
# plt.show()

# bionomial distribution
# x = random.binomial(n=10, p=0.5, size=10) #otuput: [5 6 6 7 4 7 6 9 7 6]
# x = random.binomial(n=10, p=0.9, size=10) #output: [10  9  9  7 10  9 10  9  8 10]
# print(x)

# # visualization of binomial distribution
# data = random.binomial(n=10, p=0.5, size=100)
# sns.displot(data)
# # sns.displot(data, kind="kde")
# plt.show()

