# filepath: /home/saida/IdeaProjects/data-science-project/process/Grouping%26Aggregating.py
# This script demonstrates grouping and aggregating data using pandas
import pandas as pd

# Load CSV file
df = pd.read_csv("/home/saida/IdeaProjects/data-science-project/data/tips.csv")

# Average total bill by gender
print(df.groupby('sex')['total_bill'].mean())

# Average tip by day
#print(df.groupby('day')['tip'].mean())

# Multiple aggregations by day
#print(df.groupby('day').agg({'total_bill': 'mean', 'tip': 'mean', 'size': 'sum'}))