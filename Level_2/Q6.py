def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    return n % 2 == 0 and is_power_of_two(n // 2)

if __name__ == "__main__":
    user_input = int(input("Enter a number to check if it is a power of two: "))
    
    result = is_power_of_two(user_input)
    
    if result:
        print(f"{user_input} is a power of two.")
    else:
        print(f"{user_input} is not a power of two.")