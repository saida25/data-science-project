import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

df.head()

# Inspect dataset shape and first few rows
print(df.shape)
print(df.head())

print("Get info and summary stats")
print(df.info())
print(df.describe())

print("Check missing values per column")
print(df.isnull().sum())

print("Fill missing 'Age' with median")
df['Age'].fillna(df['Age'].median(), inplace=True)

print("Fill missing 'Embarked' with mode most frequent")
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' column (too many missing)
df.drop(columns=['Cabin'], inplace=True)

print("Duplicates before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates after:", df.duplicated().sum())

import seaborn as sns
import matplotlib.pyplot as plt

# Survival rate by gender
print(df.groupby('Sex')['Survived'].mean())

# Average age by passenger class
print(df.groupby('Pclass')['Age'].mean())

# Plot survival count
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.show()
