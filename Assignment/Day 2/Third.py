# WAP to input 10 number ang get sum of all.

print("Enter 10 Numbers one by one")
sum = 0
for i in range(1, 11):
    try:
        x = int(input(f'Enter the number {i} : '))
    except:
        print("Invalid Input")
        quit()
    sum += x

print("\nThe Total SUM =", sum)
