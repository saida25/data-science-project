# Step 1: Define a list and dictionary
fruits = ["apple", "banana", "cherry"]
person = {"name": "Anita", "age": 30}

# Step 2: Access elements
print(fruits[1])         # 'banana'
print(person["name"])    # 'Anita'

# Step 3: Add new elements
fruits.append("mango")
person["city"] = "Tunis"

# Step 4: Loop through elements
for fruit in fruits:
    print(fruit)

for key, value in person.items():
    print(key, ":", value)
