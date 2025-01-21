# Taking input for the range
start = int(input("Start: "))
stop = int(input("Stop: "))

# Calculating the sum of odd numbers
sum_odds = 0
for num in range(start, stop + 1):
    if num % 2 != 0:
        sum_odds += num

# Displaying the result
print(f"Sum of odd numbers: {sum_odds}")
