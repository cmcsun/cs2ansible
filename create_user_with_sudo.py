import os
import subprocess

def create_user(username, password):
    """
    Create a new user with the given username and password.
    """
    try:
        # The password needs to be input twice for useradd, so we duplicate it with a newline in between
        subprocess.run(['useradd', '-m', username], check=True)
        subprocess.run(['passwd', username], input=f"{password}\n{password}\n".encode(), check=True)
    except subprocess.CalledProcessError:
        print(f"Error creating user {username}")
        return False
    return True

def add_to_sudoers(username):
    """
    Add the user to the sudoers file beneath the root.
    """
    sudoers_file = "/etc/sudoers"
    temp_file = "/etc/sudoers.tmp"

    with open(sudoers_file, 'r') as f:
        lines = f.readlines()

    # Find the line with root ALL=(ALL) ALL and insert the new user right below
    for i, line in enumerate(lines):
        if line.startswith('root ALL=(ALL:ALL) ALL'):
            lines.insert(i+1, f"{username} ALL=(ALL:ALL) ALL\n")
            break

    with open(temp_file, 'w') as f:
        f.writelines(lines)

    # Check the syntax of the sudoers file
    result = subprocess.run(['visudo', '-c', '-f', temp_file])
    if result.returncode == 0:
        os.rename(temp_file, sudoers_file)
    else:
        print("Error in the syntax of the sudoers file.")
        os.remove(temp_file)

if __name__ == "__main__":
    username = input("Enter the username: ")
    while True:
        password1 = input("Enter the password: ")
        password2 = input("Confirm the password: ")
        if password1 == password2:
            break
        else:
            print("Passwords do not match. Please try again.")

    if create_user(username, password1):
        add_to_sudoers(username)
