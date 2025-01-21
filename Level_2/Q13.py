starts_with = lambda s, char: s.startswith(char)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    char = input("Enter the character to check if the string starts with: ")

    result = starts_with(user_input, char)

    print(result)