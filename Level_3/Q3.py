def replace_j_with_i_in_file(filename):
    """Replaces 'J' with 'I' in the entire content of the file and updates the file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Replace 'J' with 'I'
        corrected_content = content.replace('J', 'I')

        # Write the corrected content back to the file
        with open(filename, 'w') as file:
            file.write(corrected_content)

        print(f"The content in {filename} has been updated with all 'J's replaced by 'I's.")

    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    filename = 'words.txt'  # Fixed filename
    replace_j_with_i_in_file(filename)


#this was the original file content
"""This is a sample text.
    The word 'Jelly' starts with J.
    Let's replace all the J's with I's.
    Just another example with J in it.
    Finally, the word 'Jump' contains J."""