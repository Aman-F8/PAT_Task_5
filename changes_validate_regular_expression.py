import re  # Import the regular expression module


# A. Validate E-mail Address
def validate_email_address(given_email):
    # Regular expression pattern for a valid email address
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Check if the input email matches the email pattern
    if re.match(email_pattern, given_email):
        return True  # Valid email
    else:
        return False  # Invalid email


# Get email input from user
given_email = input("Enter E-mail: ")

# Check and print result
if validate_email_address(given_email):
    print("Valid E-mail Address")
else:
    print("Invalid E-mail Address")


# --------------------------------------------------------------------------------------------------

# B. Validate Mobile Number of Bangladesh
def validate_bangladesh_number(mobile_number):
    # Valid BD mobile numbers: starts with +88 (optional), followed by 01, then digit 3-9, and 8 more digits
    mobile_pattern = r"^(?:\+88)?01[3-9]\d{8}$"

    # Check if input matches the BD mobile pattern
    if re.match(mobile_pattern, mobile_number):
        return True
    else:
        return False


# Get BD mobile number input
mobile_number = input("Enter Bangladesh Mobile Number (With or Without +88): ")

# Validate and print result
if validate_bangladesh_number(mobile_number):
    print("Valid Bangladesh mobile number")
else:
    print("Invalid Bangladesh mobile number")


# --------------------------------------------------------------------------------------------------

# C. Validate USA Mobile Number
def validate_usa_mobile_number(usa_mobile_number):
    # Pattern supports optional country code +1, optional area code parentheses, and different separators
    usa_mobile_pattern = r"^(?:\+1\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"

    # Check if input matches the US mobile number pattern
    if re.match(usa_mobile_pattern, usa_mobile_number):
        return True
    else:
        return False


# Get USA mobile number input
usa_mobile_number = input("Enter USA Mobile Number (e.g. +1 123-456-7890): ")

# Validate and print result
if validate_usa_mobile_number(usa_mobile_number):
    print("Valid USA mobile number")
else:
    print("Invalid USA mobile number")


# --------------------------------------------------------------------------------------------------

# D. Validate USA Landline Telephone Number (Same format as mobile but optional distinction)
def validate_usa_telephone_number(telephone_number):
    # Same format as mobile number - USA doesn't distinguish format-wise
    telephone_pattern = r"^(?:\+1\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"

    # Check if the number matches the telephone pattern
    if re.match(telephone_pattern, telephone_number):
        return True
    else:
        return False


# Get USA telephone number input
telephone_number = input("Enter USA Telephone Number (e.g. (123) 456-7890): ")

# Validate and print result
if validate_usa_telephone_number(telephone_number):
    print("Valid USA telephone number")
else:
    print("Invalid USA telephone number")


# --------------------------------------------------------------------------------------------------

# E. Validate Strong 16-character Password
def validate_strong_password(password):
    # Password should be exactly 16 characters and contain:
    # - At least one lowercase letter
    # - At least one uppercase letter
    # - At least one digit
    # - At least one special character
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{16}$'

    # Check if the password matches the pattern
    if re.match(password_pattern, password):
        return True
    else:
        return False


# Get password input
password = input("Enter a 16-character strong password: ")

# Validate and print result
if validate_strong_password(password):
    print("Valid Strong Password")
else:
    print("Invalid Password – must be 16 chars, mix of upper/lowercase, digit, and special char")
