import pandas as pd

# From a Dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Apply Functions
df["Age Group"] = df["Age"].apply(lambda x: "Young" if x < 30 else "Old")
print(df)

# Pivot Table
pivot = df.pivot_table(values="Age", index="City", columns="Gender", aggfunc="mean")
print(pivot)

# MultiIndex
df_multi = df.set_index(["City", "Name"])
print(df_multi)
