def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))


if __name__ == "__main__":
    list1 = input("Enter the first list of numbers, separated by spaces: ")
    list2 = input("Enter the second list of numbers, separated by spaces: ")

    list1 = list(map(int, list1.split()))
    list2 = list(map(int, list2.split()))
    
    common_elements = find_common_elements(list1, list2)
    print("Common elements:", common_elements) 