def parse_encoded_string(encoded_str):
    """Parses the encoded string and returns a dictionary."""
    parts = encoded_str.split("0")
    cleanedParts = []
    for part in parts:
        if part != '':
            cleanedParts.append(part)

    return {"first_name": cleanedParts[0], "last_name": cleanedParts[1], "id": cleanedParts[2]}

if __name__ == "__main__":
    encoded_str = input("Enter the encoded string (e.g., Robert000Smith000123): ")
    parsed_data = parse_encoded_string(encoded_str)
    print("Parsed data:", parsed_data)