import random
import base64
from colorama import Fore
import os, sys, base64, subprocess, platform
import pyfiglet


def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls",
                         shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")

# Unicode Encoding
def unicode_encode(text):
    return text.encode('utf-8')

# Unicode Decoding
def unicode_decode(encoded_text):
    return encoded_text.decode('utf-8')

# Base64 Encoding
def base64_encode(text):
    encoded_bytes = base64.b64encode(text)
    return encoded_bytes.decode('utf-8')

# Base64 Decoding
def base64_decode(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text)
    return decoded_bytes.decode('utf-8')

# Enigma Encoding
def enigma_encode(text, key):
    result = ''
    for char in text:
        if char.islower():
            encoded_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():
            encoded_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encoded_char = char
        result += encoded_char
    return result

def enigma_decode(text, key):
    result = ''
    for char in text:
        if char.islower():
            decoded_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        elif char.isupper():
            decoded_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            decoded_char = char
        result += decoded_char
    return result




# Main program
def main():
    print(Fore.GREEN + "---------------------------------------------------")
    print(Fore.WHITE + "")
    choice = input("Select an option (1: Encode, 2: Decode): ")
    print("")
    if choice == '1':
        input_text = input("Enter the text to encode: ")
        print("")
        pin = int(input("Enter the pin: "))
        print("")

        encoded_text = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')
        for _ in range(pin):
            encoded_text = enigma_encode(encoded_text, pin)

        print("Encoded text:", encoded_text)
        print("")
        main()

    elif choice == '2':
        input_text = input("Enter the text to decode: ")
        print("")
        pin = int(input("Enter the pin: "))
        print("")

        decoded_text = input_text
        for _ in range(pin):
            decoded_text = enigma_decode(decoded_text, pin)

        decoded_text = base64_decode(decoded_text)

        print("Decoded text:", decoded_text)
        print("")
        main()

    else:
        print("Invalid choice. Please try again.")
        print("")
        main()

clear()

text = "AXEL"

# Create a Figlet object with the desired font
figlet_font = pyfiglet.Figlet(font="standard")

# Render the text in ASCII art
ascii_art = figlet_font.renderText(text)

print(ascii_art)
print(Fore.RED + "Make by Bell (github.com/Bell-O)")

if __name__ == "__main__":
    main()
