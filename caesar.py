from datetime import datetime

print("This is a program for Caesar to know your name!")
name = input("What is your name?\n")

day = int(datetime.now().day)

#apply a Caesar cipher with a shift based on the current day
ciphered_name = ""
for char in name:
    if char.isalpha():
        shift = day % 26
        if char.islower():
            ciphered_name += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphered_name += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        ciphered_name += char

print("You should address yourself as:", ciphered_name, "to Caesar.")
