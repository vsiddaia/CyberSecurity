string = input("Please enter a string to encode. ")

# Convert to ASCII encoded
ascii_encoded = list()
for letter in string:
    ascii_encoded.append(ord(letter))

# Convert ASCII to binary
binary = list()
for point in ascii_encoded:
    # NOTE: Using [2:] to slice removes the '0b' prefix
    # binary.append(bin(point)[2:])
    binary.append(bin(point))

# Convert ASCII to hex
hexadecimal = list()
for point in ascii_encoded:
    hexadecimal.append(hex(point))

# Print All
print("Your string in ASCII encoding...")
for point in ascii_encoded:
    print(point, end=" ")

print("\n" + "=-" * 12)
print("Your string in hexadecimal...")
for byte in hexadecimal:
    print(byte, end=" ")

print("\n" + "=-" * 12)
print("Your string in binary...")
for bit in binary:
    print(bit, end=" ")
