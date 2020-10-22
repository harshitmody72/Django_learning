#Create a function that accept a name and return reverse of this

def reverse_name(a):
    reverse = ""
    for i in a:
        reverse = i + reverse
    return reverse


name = input("Enter the NAME ")
result = reverse_name(name)
print("\nThe Reverse name is", result.title())
