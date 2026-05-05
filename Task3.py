# Password Generator

import random

print("Welcome to Password Generator")
print("This will make a strong password for you")
print("")

# all the letters and stuff for password
small_letters = "abcdefghijklmnopqrstuvwxyz"
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# put them all together
all_characters = small_letters + big_letters + numbers + special

# ask how long the password should be
while True:
    length_input = input("How long should the password be? (at least 8): ")
    try:
        password_length = int(length_input)
        if password_length >= 8:
            break
        else:
            print("Password must be at least 8 characters long")
    except:
        print("Please enter a number")

# make the password
password = ""
for i in range(password_length):
    # pick a random character
    random_char = random.choice(all_characters)
    # add it to password
    password = password + random_char

print("")
print("Here is your password:")
print(password)
print("")
print("Remember to save this password somewhere safe!")