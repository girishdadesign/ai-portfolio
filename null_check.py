import pandas as pd

df = pd.read_csv("customers.csv")  # swap in one of your own file names
null_counts = df.isnull().sum()
print(null_counts[null_counts > 0])

# Bonus exercise: add this line yourself and run it again on a real file from work.
# print(df.duplicated().sum())
