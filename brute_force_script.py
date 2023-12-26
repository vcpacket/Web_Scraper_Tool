# Author: VCPacket
# Enhanced PDF brute force script
# Generates passwords with any combination of numbers, upper and lower case alphabets, and special characters.

import sys
import string
import random
import fitz  # PyMuPDF

def generate_random_password():
    # Generate a random password of length between 8 and 16 characters
    password_length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(password_length))

# Display help message
helpmsg = "Enhanced PDF brute force script\n"
helpmsg += "Example: Password123!\n\n"
helpmsg += "Usage: pdfbrute.py"

print(helpmsg)

# Prompt the user for the PDF file name
pdf_file_path = input("Enter the path to the encrypted PDF file: ")

try:
    pdf_doc = fitz.open(pdf_file_path)
except FileNotFoundError:
    print("[!] File not found. Please check the file path and try again.")
    sys.exit()

# Check if the PDF is encrypted
if pdf_doc.needs_pass:
    print("[+] PDF is encrypted. Attempting to Brute force. This could take some time...")

    while True:
        password_attempt = generate_random_password()

        if pdf_doc.authenticate(password_attempt):
            print("[+] Password found: " + password_attempt)
            sys.exit()

    # The loop will continue until the correct password is found, so this line is unreachable
    # print("[!] Password not found in the given range.")
else:
    print("[!] The file is not protected with any password. Exiting.")
    sys.exit()
