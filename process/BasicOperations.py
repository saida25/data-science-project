# Variables
name = "Saida"
age = 25  # Change to your real age
height = 1.75  # In meters
is_beginner = True
# Math operations
print("\n🧮 Math Operations:")
print(f"Age in 5 years: {age + 5}")
print(f"Height in cm: {height * 100:.0f}")
print(f"Half your age: {age / 2}")

# String operations
print("\n🔤 String Operations:")
print(f"Name repeated: {name * 3}")
print(f"Name uppercase: {name.upper()}")

# User interaction
print("\n💬 Let's get to know each other!")
user_name = input("What's your name? ")
user_age = int(input("How old are you? "))
user_height = float(input("Your height in meters? "))

print(f"\n👋 Hello {user_name}! Here's your profile:")
print(f"• You'll be {user_age + 5} in 5 years")
print(f"• Your height is {user_height*100:.0f} cm")
if user_age < 30:
    print("• You're young in the AI field!")
else:
    print("• Your experience is valuable in AI!")