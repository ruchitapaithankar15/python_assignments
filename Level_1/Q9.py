# Taking input from the user
lst = input("Enter the input list (separated by spaces): ").split()

# Counting the frequency of each element
frequency = {}
for item in lst:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

# Displaying the frequency of each element
print("Frequency:", frequency)
