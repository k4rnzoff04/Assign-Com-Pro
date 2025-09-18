import pandas as pd

data = {"Name" : ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City" : ["New york", "Los Angeles", "Chicago"]
        }

df = pd.DataFrame(data)
print(f"DataFrame : \n {df}")

average_age = df["Age"].mean()
print(f"\nAverage Age: {average_age}")

filtered_df = df[df["Age"] > 28]
print(f"\nFiltered DataFrame (Age > 28): \n {filtered_df}")

df["Salary"] = [50000, 60000, 70000]
print(f"\nDataFrame with Salary column:\n {df}")