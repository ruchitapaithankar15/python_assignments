def count_lines(filename):
    """Counts the number of lines in a file."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0

if __name__ == "__main__":
    filename = 'demo.txt'  # Fixed filename
    num_lines = count_lines(filename)
    print(f"Number of lines in the file: {num_lines}")
