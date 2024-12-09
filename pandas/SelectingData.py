# Selecting Data
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Selecting Columns
print(df["Name"])  # Single column
print(df[["Name", "Age"]])  # Multiple columns

# Selecting Rows
print(df.iloc[0])  # First row by index
print(df.loc[0])   # First row by label

# Filtering Rows
adults = df[df["Age"] > 30]  # Rows where Age > 30
print(adults)

# Conditional Filtering
ny_residents = df[(df["Age"] > 25) & (df["City"] == "New York")]
print(ny_residents)
