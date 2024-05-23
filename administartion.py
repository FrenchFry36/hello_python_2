#os.system
#subprocess.run

import os

def add_user():
    username = input("Enter the name of the user to add: ")

    check_user = os.system (f"getent psswd {username}")

    if check_user == 0:
        print(f"The username '{username}' already exists")
        return
    
    confirm = input(f"Do you want to add {username} to the system?")

    if confirm == 'y':

        result = os.system(f"sudo useradd -m {username}")

        if result == 0:
            print(f"User {username} added successfully!")
        else:
            print(f"Failed to add user {username}")
    else:
        print("User addition cancelled")

if __name__ == "__main__":
    add_user()