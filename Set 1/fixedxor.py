# 1.2: Take two equal-length buffers and produce their XOR combination
from math import *

# Given two hexadecimal strings h1, h2, produce their XOR combination
def hex_xor(h1, h2):
	h1 = int(h1,16)
	h2 = int(h2,16)

	xor = h1 ^ h2

	hex_str = str(hex(xor))[2:]

	if len(hex_str) % 2 != 0:
		hex_str = "0" + hex_str

	hex_out = bytes.fromhex(hex_str)

	return hex_out

# The challenge: 
# print(hex_xor("1c0111001f010100061a024b53535009181c",
# 			  "686974207468652062756c6c277320657965").hex())