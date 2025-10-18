import random
import string

print("PASSWORD GENERATOR")

# Ask the user for the desired password length
length = int(input("Enter the desired password length: "))

# Define the characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation
# (ascii_letters = A-Z and a-z, digits = 0-9, punctuation = symbols like @, #, $, etc.)

# Generate a random password
password = ''.join(random.choice(characters) for i in range(length))

# Display the generated password
print("\n Your generated password is:", password)
