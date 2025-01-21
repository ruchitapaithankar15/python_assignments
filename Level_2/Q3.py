def count_pairs_with_sum(arr, k):
    seen = {}
    count = 0
    for num in arr:
        complement = k - num
        if complement in seen:
            count += 1
        seen[num] = True
    return count

if __name__ == "__main__":
    user_input = input("Enter the elements of the array, separated by spaces: ")
    k = int(input("Enter the value of k: "))
    arr = list(map(int, user_input.split()))
    pair_count = count_pairs_with_sum(arr, k)
    print("Pair count:", pair_count)