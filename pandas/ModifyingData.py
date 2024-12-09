import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)


# Adding a Column
df["Salary"] = [70000, 80000, 90000]
print(df)

# Renaming Columns
df.rename(columns={"Name": "Full Name", "Age": "Years"}, inplace=True)
print(df)

# Dropping Columns
df.drop(columns=["Salary"], inplace=True)
print(df)

# Updating Values
df.loc[0, "Age"] = 26  # Update specific value
print(df)
