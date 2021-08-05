"""
A website requires the users to input username and password to register. Write a program to check the validity of
password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.

Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:
ABd1234@1
"""


def is_lower(string):
    for char in string:
        if 'a' <= char <= 'z':
            return True
    return False


def is_upper(string):
    for char in string:
        if 'A' <= char <= 'Z':
            return True
    return False


def is_digit(string):
    for char in string:
        if '0' <= char <= '9':
            return True
    return False


def is_special(string):
    special_characters = '"!@#$%^&*()-+?_=,<>/"'
    for char in string:
        if char in special_characters:
            return True
    return False


password = list(map(str, input().split(",")))
new_list = []

for value in password:
    if 6 <= len(value) <= 12:
        if is_lower(value) and is_digit(value) and is_upper(value) and is_special(value):
            new_list.append(value)

print(" ".join(new_list))