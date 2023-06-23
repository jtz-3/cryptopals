# 1.1: Convert hex strings to base64

from base64 import *

# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

hex_input = input("Enter a hex string: ")

# Prepend a 0, if necessary, to make the string suitable for 
# 	interpretation as a hexadecimal value
if len(hex_input) % 2 != 0:
	hex_input = "0" + hex_input

# Convert a hexadecimal input to a bytes objet
hex_bytes = bytes.fromhex(hex_input)
# print(hex_bytes)

b64 = b64encode(hex_bytes).decode()
print("Output in base64: ", b64)