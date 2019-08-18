string = input("Please enter a string to encode. ")

# Convert to ASCII encoded
ascii_encoded = [ord(letter) for letter in string]

# Convert ASCII to hex
hexadecimal = [hex(ascii_value) for ascii_value in ascii_encoded]

# Convert ASCII to binary
binary = [bin(ascii_value) for ascii_value in ascii_encoded]

# Convert ASCII to octal
octal = [oct(ascii_value) for ascii_value in ascii_encoded]

# Print All
print("Your string in ASCII encoding...")
for point in ascii_encoded:
    print(point, end=" ")

print("\n" + "=-" * 12)
print("Your string in hexadecimal...")
for byte in hexadecimal:
    print(byte, end=" ")

print("\n" + "=-" * 12)
print("Your string in octal...")
for octet in octal:
    print(octet, end=" ")

print("\n" + "=-" * 12)
print("Your string in binary...")
for bit in binary:
    print(bit, end=" ")
