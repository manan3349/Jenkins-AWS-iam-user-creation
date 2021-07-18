#!/usr/bin/python3
## AWS credentials should be configured in CLI or in jenkins
## Configured user should have appropriate policies to create user, modify user and add user to group

import boto3
import sys
import json
import secrets
import string
from botocore.exceptions import ClientError

## Checking for parameters username, groupname and ssh key to be added
if len(sys.argv) != 6:
	print("Usage:")
	print(f"{' '*4} {sys.argv[0]} [USERNAME] [GROUPNAME] [SSH_KEY]")
	sys.exit(1)

## Assigning arguments to global variables
USER = str(sys.argv[1])
GRP = str(sys.argv[2])
SSH_KEY = " ".join(sys.argv[3:5])

## Create a low-level service client by name using the default session.
client = boto3.client('iam')

## Creating IAM user
try:
    client.create_user(UserName=USER)
    print("User Created :",USER)
except ClientError as err:
    if err.response['Error']['Code'] == 'EntityAlreadyExists':
        sys.stderr.write("Error: User with the same name already exists\n")
    elif err.response['Error']['Code'] == 'ValidationError':
        sys.stderr.write("Error: The specified value for userName is invalid.\n")
    else:
        sys.stderr.write("Error: Unexpected error occured while creating user\n")
    sys.exit(1)

## Creating password for user
s = string.ascii_letters+string.digits+string.ascii_uppercase+string.ascii_lowercase+string.punctuation
pasw = "".join(secrets.choice(s) for _ in range(16))
try:
	client.create_login_profile(UserName=USER,Password=pasw,PasswordResetRequired=True)
	print("User Password :",pasw)
except ClientError as err:
    if err.response['Error']['Code'] == 'EntityAlreadyExists':
        sys.stderr.write("Error: Password for the user already exists\n")
    elif err.response['Error']['Code'] == 'NoSuchEntity':
        sys.stderr.write("Error: The specified user doesn't exist.\n")
    elif err.response['Error']['Code'] == 'PasswordPolicyViolation':
        sys.stderr.write("Error: The provided password did not meet the requirements imposed by the account password policy.\n")
    else:
        sys.stderr.write("Error: Unexpected error occured while creating user\n")
    sys.exit(1)

## Getting acoount alias
print("Account ID :",boto3.client('sts').get_caller_identity().get('Account'))

## Adding created user to predefined groups
try:
    client.add_user_to_group(GroupName=GRP,UserName=USER)
    print("User added to group :",GRP)
except:
    sys.stderr.write("Error: Unexpected error occured while adding user to group\n")
    sys.exit(1)

## Uploading SSH Public key for created user
try:
    client.upload_ssh_public_key(UserName=USER,SSHPublicKeyBody=SSH_KEY)
    print("SSH Key access added")
except ClientError as err:
    if err.response['Error']['Code'] == 'InvalidPublicKey':
        sys.stderr.write("Error: Invalid Public Key\n")
    elif err.response['Error']['Code'] == 'DuplicateSSHPublicKey':
        sys.stderr.write("Error: SSH key already associated with the user\n")
    elif err.response['Error']['Code'] == 'UnrecognizedPublicKeyEncoding':
        sys.stderr.write("Error: The public key encoding format is unsupported, only ssh-rsa or PEM format allowed\n")
    else:
        sys.stderr.write("Error: Unexpected error occured while adding SSH Key\n")
    sys.exit(1)
print("Completed")
