import pandas as pd

# Load CSV file
df = pd.read_csv("/home/saida/IdeaProjects/data-science-project/data/titanic.csv")

# First 5 rows
#print(df.head())

# Dataset shape
#print("Shape:", df.shape)

# Column names
#print("Columns:", df.columns.tolist())

# Info about data types
#print(df.info())

# Summary statistics
print(df.describe())
