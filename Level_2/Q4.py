def rotate_array(arr, d):
    if not arr:  # Handle empty array
        return arr
    d = d % len(arr) 
    return arr[-d:] + arr[:-d]

if __name__ == "__main__":
    user_input = input("Enter the elements of the array, separated by spaces: ")
    d = int(input("Enter the number of elements to rotate: "))

    arr = list(map(int, user_input.split()))

    rotated_array = rotate_array(arr, d)

    print("Array after rotation:", rotated_array)