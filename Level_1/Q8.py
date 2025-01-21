# Taking input from the user
a = int(input("number1: "))
b = int(input("number2: "))

# Finding the greater number
greater = max(a, b)

# Calculating the LCM
while True:
    if greater % a == 0 and greater % b == 0:
        print(f"The LCM of {a} and {b} is: {greater}")
        break
    greater += 1
