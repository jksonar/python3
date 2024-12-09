# Inspecting Data

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Basic Information
print(df.info())  # Summary of DataFrame
print(df.describe())  # Statistics for numeric columns

# Checking Head and Tail
print(df.head())  # First 5 rows
print(df.tail(3))  # Last 3 rows

# Viewing Columns and Index
print(df.columns)  # List of column names
print(df.index)    # RangeIndex of rows
