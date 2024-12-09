# Working with Time Series Data
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Parsing Dates
df = pd.read_csv("data.csv", parse_dates=["Date"])
print(df.info())

# Setting a Datetime Index
df.set_index("Date", inplace=True)

# Resampling
monthly = df.resample("M").mean()  # Resample to monthly average
print(monthly)
