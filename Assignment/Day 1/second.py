# Program to input 2 number and swap them
try:
    first = int(input("Enter the first number :"))
    second = int(input("\nEnter the second number :"))
except:
    print("Invalid Input")
    quit()

print("\nNumber's Before swapping ")
print("First number = ", first)
print("Second number = ", second)

first = first + second
second = first - second
first = first - second

print("\nNumber's After swapping ")
print("First number = ", first)
print("Second number = ", second)
