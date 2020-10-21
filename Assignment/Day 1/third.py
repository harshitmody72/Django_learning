# Program to input number and test it is even or odd

try:
    n = int(input("Enter a number :"))
except:
    print("Invalid Input")
    quit()

if (n % 2 == 0):
    print(f"Entered number {n} is Even ")
else:
    print(f"Entered number {n} is Odd")
