# Taking input from the user
num = int(input("Enter a number to check if it is a perfect number: "))

# Finding divisors and checking if the number is perfect
divisors_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisors_sum += i

# Determining if the number is perfect
if divisors_sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
