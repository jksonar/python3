import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# group by

grouped = df.groupby("City").mean()
print(grouped)

# Aggregation
print(df.groupby("City")["Age"].agg(["mean", "max", "min"]))
