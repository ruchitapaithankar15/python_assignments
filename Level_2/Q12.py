def login_system():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for _ in range(3):
        retype_password = input("Re-Type password: ")
        if retype_password == password:
            print("Login successful!")
            return
        print("Passwords do not match. Try again.")
    print("Login failed. Too many attempts.")

if __name__ == "__main__":
    login_system()
