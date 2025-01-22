def read_and_append_even_length_strings():
    filename = 'doc.txt'
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Extract even length words
        even_length_words = []
        for line in lines:
            words = line.split()
            for word in words:
                if len(word) % 2 == 0:
                    even_length_words.append(word)
        
        # Append the even length words to the file
        with open(filename, 'a') as file:  # Open the file in append mode
            file.write("\nEven length words:\n")  # Add a section title
            for word in even_length_words:
                file.write(word + "\n")  # Write each word on a new line

        print(f"Even length words have been appended to {filename}.")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    read_and_append_even_length_strings()
