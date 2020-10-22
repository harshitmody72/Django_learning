# WAP to input and print table of that.

try:
    x = int(input("Enter the First Number: "))

except:
    print("Invalid Input")
    quit()

    
print("\n Table \n")
for i in range(1, 11):
    print(f'{x} * {i} =', x*i)
