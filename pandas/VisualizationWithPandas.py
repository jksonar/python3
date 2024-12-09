import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Plotting
df.plot(x="Name", y="Salary", kind="bar", title="Salaries of Employees")
plt.xlabel("Employee Name")
plt.ylabel("Salary ($)")
plt.show()
