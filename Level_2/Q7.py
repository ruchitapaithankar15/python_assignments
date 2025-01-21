def find_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

if __name__ == "__main__":

    user_input = input("Enter the numbers in the list, separated by spaces: ")

    number_list = list(map(int, user_input.split()))

    median = find_median(number_list)

    print(f"The median is: {median}")