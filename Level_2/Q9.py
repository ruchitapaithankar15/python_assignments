def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

if __name__ == "__main__":
    user_input = input("Enter the list elements, separated by spaces: ")
    lst = list(map(int, user_input.split()))
    index = int(input("Enter the index to access: "))

    result = safe_list_access(lst, index)

    print(f"Result: {result}")