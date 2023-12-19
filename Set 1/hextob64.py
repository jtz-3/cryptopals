# 1.1: Convert hex strings to base64

from base64 import *

# Given a hexadecimal string hex_str, output the bytes of hex_str converted to base 64
def hex_to_base_64(hex_str):
	if len(hex_str) % 2 != 0:
		hex_str = "0" + hex_str

	# Convert a hexadecimal input to a bytes objet
	hex_bytes = bytes.fromhex(hex_str)

	b64 = b64encode(hex_bytes)

	return b64

# test = input("Enter a hex string: ")
# print("Output in base64: ", hex_to_base_64(test).decode())
