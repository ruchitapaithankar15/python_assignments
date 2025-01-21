# Taking input from the user
n = int(input("Enter a number to calculate its factorial: "))

# Calculating factorial using a for loop
result = 1
for i in range(1, n + 1):
    result *= i

# Displaying the result
print(f"The factorial of {n} is: {result}")
