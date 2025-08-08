import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

df.head()

# Inspect dataset shape and first few rows
print(df.shape)
print(df.head())

# Get info and summary stats
print(df.info())
print(df.describe())
