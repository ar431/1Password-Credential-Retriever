# 1Password-Credential-Retriever

A Python script to securely retrieve usernames and passwords from 1Password using the CLI.

## Usage

```sh
python script.py <op_path> <item_name>
```
### Parameters
<op_path>: The file path to the op executable.

<item_name>: The name of the 1Password item to retrieve.

### Environment Variables

OP_ACCOUNT: The 1Password account name. This is optional for single-account use cases. If you have multiple accounts, set this variable to specify which account to use.

#### Example
```sh
# Set the environment variable for account name without quotations (optional)
SET OP_ACCOUNT=your_account_name

# Run the Script
python3 main.py "</Path/to/op.exe>" "<1Password Credential Name>"
```
## Requirements
Python 3.x

1Password CLI (op)

## Installation
Install the 1Password CLI from [1Password CLI documentation](https://developer.1password.com/docs/cli/get-started/).
Ensure the op executable is accessible in your system PATH or provide the full path to the executable.

## Notes
This script requires the user to be signed in to their 1Password account.
Handle the credentials securely and avoid exposing them in logs or console outputs.
The OP_ACCOUNT environment variable is optional and only needed if you have multiple 1Password accounts. If not set, the script assumes a single account context.

