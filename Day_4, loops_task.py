# Day 4 - Python Loops Project

print("---- Simple Loop Programs ----")

# Program 1: Print numbers from 1 to 10
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# Program 2: Print name 5 times
print("\nPrint Name 5 Times:")
name = input("Enter your name: ")
for i in range(5):
    print("My name is", name)

# Program 3: Multiplication Table
print("\nMultiplication Table:")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\n--- Program Completed Successfully ---")
