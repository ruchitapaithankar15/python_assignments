def run_length_encoding(input_string):
    result = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i-1]:
            count += 1
        else:
            result.append(f"{input_string[i-1]}{count}")
            count = 1
    result.append(f"{input_string[-1]}{count}")
    return ''.join(result)

if __name__ == "__main__":
    input_string = input("Enter the string for run-length encoding: ")
    encoded_string = run_length_encoding(input_string)
    print("Encoded string:", encoded_string)