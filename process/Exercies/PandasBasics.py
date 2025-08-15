import pandas as pd

data = {
    "Name": ["Anita", "Sara", "Omar"],
    "Age": [28, 24, 30],
    "Country": ["Tunisia", "Algeria", "Morocco"]
}

df = pd.DataFrame(data)

print(df)
#print(df.head())          # First 5 rows
#print(df.describe())      # Summary statistics
#print(df.info())          # Data types
#print(df["Name"])           # Access column
print(df.loc[0])            # Access row by label
print(df.iloc[1])           # Access row by index
print(df.iloc[2])  # Third row
print(df.iloc[0:3])
