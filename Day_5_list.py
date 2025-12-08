# Day 6 - Python List Project

print("---- List Program ----")

# Create a list
fruits = ["apple", "banana", "mango"]

# Print full list
print("Fruits:", fruits)

# Print first fruit
print("First fruit:", fruits[0])

# Add a new fruit
new_fruit = input("Enter a new fruit name: ")
fruits.append(new_fruit)

# Print updated list
print("Updated fruit list:")
for fruit in fruits:
    print(fruit)

print("---- Program Completed ----")
