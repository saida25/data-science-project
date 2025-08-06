import pandas as pd

data = {
    "Name": ["Anita", "Sara", "Omar"],
    "Age": [28, 24, 30],
    "Country": ["Tunisia", "Algeria", "Morocco"]
}

df = pd.DataFrame(data)

print(df)
