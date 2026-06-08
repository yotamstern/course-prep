import re
import string

class UsernameContainsIllegalCharacter(Exception):
    def __str__(self):
        return "The username contains an illegal character"

class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"

class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character (requires uppercase, lowercase, number, and punctuation)"

class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"

class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"

def check_username(username):
    if len(username) < 3:
        raise UsernameTooShort
    if len(username) > 16:
        raise UsernameTooLong
    if not re.fullmatch(r'\w+', username):
        raise UsernameContainsIllegalCharacter

    return True


def check_password(password):
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    if not (has_lower and has_special and has_upper and has_digit):
        raise PasswordMissingCharacter


def check_input(username, password):
        check_username(username)
        check_password(password)
        print("Result = OK")







def main():
    test_cases = [
        ("1", "2"),
        ("0123456789ABCDEFG", "2"),
        ("A_a1.", "12345678"),
        ("A_1", "2"),
        ("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary"),
        ("A_1", "abcdefghijklmnop"),
        ("A_1", "ABCDEFGHIJLKMNOP"),
        ("A_1", "ABCDEFGhijklmnop"),
        ("A_1", "4BCD3F6h1jk1mn0p"),
        ("A_1", "4BCD3F6.1jk1mn0p")
    ]

    for username, password in test_cases:
        try:
            print(f"\n\nChecking username and password for... \nUser Name: {username} \nPassword: {password} ")
            check_input(username, password)
        except Exception as e:
            print(f"Result = Failed \nRaised Error: {e}")



if __name__ == "__main__":
    main()

