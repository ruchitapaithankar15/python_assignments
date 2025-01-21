def get_unique_elements(array):
    return list(set(array))

if __name__ == "__main__":
    user_input = input("Enter the elements of the list, separated by spaces: ")
    lst = list(map(int, user_input.split()))
    unique_elements = get_unique_elements(lst)
    print("Unique elements:", unique_elements)