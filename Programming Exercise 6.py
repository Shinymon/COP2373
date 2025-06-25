"""
This script validates user input for U.S. phone numbers, Social Security Numbers (SSNs),
and ZIP codes using regular expressions.

It includes:
- Functions to validate each type of input.
- A main function that asks the user to enter each value and checks if it's valid.
- A test suite with example inputs (both valid and invalid) to demonstrate the behavior.

Supported formats:
- Phone: (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890, +1 123 456 7890
- SSN: 123-45-6789
- ZIP: 12345 or 12345-6789
"""

import re

# Function to validate US phone numbers
def is_valid_phone(phone):
    """
    Validates US phone numbers with formats:
    (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890, +1 123 456 7890
    """
    pattern = re.compile(r'^(\+1\s?)?(\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}$')
    return bool(pattern.match(phone))

# Function to validate Social Security Numbers
def is_valid_ssn(ssn):
    """
    Validates SSNs in the format: 123-45-6789
    """
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

# Function to validate ZIP codes
def is_valid_zip(zip_code):
    """
    Validates US ZIP codes: 5-digit or ZIP+4
    """
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

# Main function to interact with user
def main():
    print("Enter the following information:")

    phone = input("Phone number: ")
    ssn = input("Social Security Number : ")
    zip_code = input("ZIP Code: ")

    # Validate each input
    print("\nValidation Results:")
    print(f"Phone number valid: {is_valid_phone(phone)}")
    print(f"SSN valid: {is_valid_ssn(ssn)}")
    print(f"ZIP code valid: {is_valid_zip(zip_code)}")

# Test cases for validation (simulates unit testing)
def run_tests():
    print("\nRunning test cases...\n")

    phone_tests = [
        "123-456-7890", "(123) 456-7890", "123.456.7890", "1234567890", "+1 123 456 7890", "12-3456-789", "phone123"
    ]
    ssn_tests = [
        "123-45-6789", "000-00-0000", "12-345-6789", "123456789", "abc-de-fghi"
    ]
    zip_tests = [
        "12345", "12345-6789", "1234", "123456", "12345-678", "ZIP123"
    ]

    print("Phone Number Tests:")
    for phone in phone_tests:
        print(f"{phone}: {is_valid_phone(phone)}")

    print("\nSSN Tests:")
    for ssn in ssn_tests:
        print(f"{ssn}: {is_valid_ssn(ssn)}")

    print("\nZIP Code Tests:")
    for zip_code in zip_tests:
        print(f"{zip_code}: {is_valid_zip(zip_code)}")

# Run the main program and tests
if __name__ == "__main__":
    main()
    run_tests()