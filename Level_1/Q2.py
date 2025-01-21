# Taking input from the user
string = input("Enter a string: ")

# Initializing counters
letters = 0
digits = 0

# Counting letters and digits
for c in string:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1

# Printing the result
print(f"Alphabets: {letters} & Numbers: {digits}")
