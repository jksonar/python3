import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Checking for Missing Values
print(df.isnull().sum())  # Count missing values in each column

# Filling Missing Values
df["Age"].fillna(df["Age"].mean(), inplace=True)  # Fill NaNs with mean

# Dropping Missing Values
df.dropna(inplace=True)  # Drop rows with NaNs
