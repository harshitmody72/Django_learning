# Create a function that return sum of two numbers if numbers are >=10.

def sum(a, b):
    return a+b


try:
    x = float(input("Enter the First Number: "))
    y = float(input("Enter the Second Number: "))

except:
    print("Invalid Input")
    quit()

if x < 10 and y < 10:
    print("Invalid Input")
    quit()


result = sum(x, y)
print("\nThe Total SUM =", result)
