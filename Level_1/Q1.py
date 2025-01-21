# Divisible by 3 and 5
# Taking input from the user
num = int(input("Enter a number: "))

# Checking divisibility
if num % 3 == 0 and num % 5 == 0:
    print("Consultadd - Python Training")
elif num % 3 == 0:
    print("Consultadd")
elif num % 5 == 0:
    print("Python Training")
else:
    print("Not divisible by 3 or 5")