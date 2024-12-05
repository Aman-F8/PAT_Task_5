#A.E-mail Address
import re
# Function to validate email
# Regular expression pattern for a valid email address
def validate_email_address(given_email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # Check if the email matches the regex pattern
    if re.match(email_pattern, given_email):
        return True
    else:
        return False

given_email = input("Enter E-mail:")

if validate_email_address(given_email):
    print("Valid E-mail Address")
else:
    print("Invalid E-mail Address")

#B. Mobile Number of Bangladesh
def validate_bangladesh_number(mobile_number):
    mobile_pattern = r"^(?:\+88)?01[3-9]\d{8}$"
    # Check if the email matches the regex pattern
    if re.match(mobile_pattern, mobile_number):
        return True
    else:
        return False

mobile_number = input("Enter Mobile Number With Country Code:")

if validate_bangladesh_number(mobile_number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

#C. Telephone Number of Bangladesh
def validate_usa_number(usa_mobile_number):
    usa_mobile_pattern = r"^(?:\+1\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    # Check if the email matches the regex pattern
    if re.match(usa_mobile_pattern, usa_mobile_number):
        return True
    else:
        return False

usa_mobile_number = input("Enter Mobile Number With Country Code:")

if validate_usa_number(mobile_number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")




