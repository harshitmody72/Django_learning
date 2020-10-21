# Program to input name and marks of 5 subject and then print percentage.

name = input("Enter your name : ")
try:
    sum = 0
    print("\nEnter the marks of 5 subject \n")
    for i in range(1, 6):
        m = int(input(f"marks of subject {i} out 0f 100 : "))
        sum += m
except:
    print("\nInvalid input")
    quit()

average = sum/500
percentage = average*100
print("\nPercentage = %.2f" % (percentage),"%")
