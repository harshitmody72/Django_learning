# WAP to input 3 numbers and print highest number amoung them.

try:
    x = float(input("Enter the First Number: "))
    y = float(input("Enter the Second Number: "))
    z = float(input("Enter the Third Number: "))

except:
    print("Invalid input")
    quit()

if x >= y and x >= z:
    print("Enterd number", x, "is highest")
elif y >= z:
    print("Enterd number", y, "is highest")
else:
    print("Enterd number", z, "is highest")
