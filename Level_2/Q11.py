def split_strings(strings):
    return list(map(list, strings))

if __name__ == "__main__":
    user_input = input("Enter strings separated by commas: ")
    strings = user_input.split(", ")
    split_list = split_strings(strings)
    print(f"List of individual strings: {split_list}")