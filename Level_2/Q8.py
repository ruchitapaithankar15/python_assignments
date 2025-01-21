def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

if __name__ == "__main__":
    user_input = input("Enter a string to count vowels: ")

    vowel_count = count_vowels(user_input)

    print(f"Number of vowels: {vowel_count}")