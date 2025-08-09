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
#print(df.describe())

# Count missing values
#print(df.isnull().sum())

# Fill missing Age with mean
#df['age'].fillna(df['age'].mean(), inplace=True)
 
#print("Missing values after filling Age:", df.isnull().sum())

# Drop rows where 'embarked' is missing
#df.dropna(subset=['embarked'], inplace=True)

# Remove duplicates
#df.drop_duplicates(inplace=True)
  
# Select a column
ages = df['age']
print(ages.head())

# Select multiple columns
subset = df[['sex','age', 'survived']]
print(subset.head())

# Filter: Passengers older than 30
older_than_30 = df[df['age'] > 30]
print(older_than_30.shape)



print("Shape after cleaning:", df.shape)
# Save cleaned data to a new CSV file   
df.to_csv("/home/saida/IdeaProjects/data-science-project/data/titanic_cleaned.csv", index=False)      
df.to_excel("titanic_cleaned.xlsx", index=False)
subset.to_csv("/home/saida/IdeaProjects/data-science-project/data/titanic_subset.csv", index=False)      