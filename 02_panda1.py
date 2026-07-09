import pandas as pd
# a = [1,7,5]
# # x = pd.Series(a)
# x = pd.Series(a, index=["x", "y" ,"z"])
# print(x)

# dataframes

data = {
    "calories": [353,235,234],
    "duration": [20, 30, 40]
}
a = pd.DataFrame(data)

print(a)
