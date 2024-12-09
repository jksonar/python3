# Merging and Joining

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Merging
data2 = {
    "Name": ["Alice", "Charlie"],
    "Department": ["HR", "IT"]
}
df2 = pd.DataFrame(data2)
merged = pd.merge(df, df2, on="Name", how="inner")  # Inner join
print(merged)

# Concatenation
df_combined = pd.concat([df, df2], axis=0)  # Concatenate rows
print(df_combined)

