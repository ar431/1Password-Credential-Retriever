import re
import subprocess
import sys
import os


def get_1pass_creds(op_path, item_name):
    """
    Retrieves the username and password for a given 1Password item.

    Parameters:
    op_path (str): The file path to the op executable.
    item_name (str): The name of the 1Password item to retrieve.

    Returns:
    tuple: A tuple containing the username and password.
    """
    try:
        # Get the item and capture the output
        result = subprocess.run([op_path, 'item', 'get', item_name], capture_output=True, text=True)
        output = result.stdout

        # Extract the username and password
        username = None
        password = None

        username_match = re.search(r'username:\s+(.*)', output)
        password_match = re.search(r'password:\s+(.*)', output)

        if username_match:
            username = username_match.group(1).strip()

        if password_match:
            password = password_match.group(1).strip()

        return username, password
    except Exception as e:
        print(f"Error retrieving credentials: {e}")
        return None, None


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <op_path> <item_name>")
        sys.exit(1)

    op_path = sys.argv[1]
    item_name = sys.argv[2]
    account_name = os.getenv('OP_ACCOUNT')

    try:
        signin_command = [op_path, 'signin']
        if account_name:
            signin_command.extend(['--account', account_name])

        subprocess.run(signin_command, check=True)
        username, password = get_1pass_creds(op_path, item_name)
        if username and password:
            #Printing Credentials to CLI is solely for testing, do not use in production
            print(f"Username: {username}\nPassword: {password}")
        else:
            print("Failed to retrieve credentials.")
    except subprocess.CalledProcessError as e:
        print(f"Signin failed: {e}")
