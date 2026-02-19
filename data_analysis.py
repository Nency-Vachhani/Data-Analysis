import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

grouped_data = df.groupby("Department")["Sales"].sum()

print("\nTotal Sales by Department:")
print(grouped_data)
