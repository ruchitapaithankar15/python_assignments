# Taking input from the user
num = int(input("Enter a number: "))

# Reversing the number
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

# Displaying the result
print(f"Reversed number: {rev}")
