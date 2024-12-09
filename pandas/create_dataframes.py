# Creating DataFrames

import pandas as pd

# From a Dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# From a CSV File
df = pd.read_csv("data.csv")
print(df.head())  # Print first 5 rows

# From a List of Lists
data = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 35, "Chicago"]]
df = pd.DataFrame(data, columns=["Name", "Age", "City"])
print(df)
