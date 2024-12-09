# Exporting Data
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Export to CSV
df.to_csv("output.csv", index=False)

# Export to Excel
df.to_excel("output.xlsx", index=False)
