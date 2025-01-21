# Taking input from the user
num = int(input("Enter a number: "))

# Calculating the sum of digits to a single digit
while num > 9:
    temp = 0
    while num > 0:
        temp += num % 10
        num //= 10
    num = temp

# Displaying the result
print(f"Single digit sum: {num}")
