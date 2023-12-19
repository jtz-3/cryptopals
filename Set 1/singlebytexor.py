from fixedxor import *

cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# Given a string txt, return the most frequently occurring character
def most_frequent_char(txt):
	if len(txt) == 0:
		raise ValueError("Cannot determine most frequent character in an empty string")

	freq_list = {}

	for i in txt:
		if i in freq_list:
			freq_list[i] += 1
		else:
			freq_list[i] = 1

	most_frequent = max(freq_list, key = freq_list.get)
	return most_frequent


# Given a plaintext txt, rate it on a scale from 0 to 25 based on its most frequent character
def score_plaintext(txt):
	txt = txt.replace(" ","")	# Remove spaces

	# Frequency table: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html)
	letters = ['z', 'j', 'q', 'x', 'k', 'v', 'b', 'p', 'g', 'w', 'y', 'f', 'm', 'c', 'u', 'l', 'd', 'h', 'r', 's', 'n', 'i', 'o', 'a', 't', 'e']

	score = -1 # If the most frequent is a non-alphabetic character, the message is likely gibberish
	most_freq = most_frequent_char(txt)


	for i in range(0,26):
		if most_freq == letters[i]:
			score = i

	return score

# Given a hex-encoded ciphertext, return a list of possible decryptions (sorted in order from
# most likely to least)
def decipher_single_byte_xor(ciphertext):
	plain_list = []

	if len(ciphertext) % 2 != 0:
		ciphertext = "0" + ciphertext
	ciphertext_length = len(ciphertext)

	# 65-91: lowercase
	# 97-123: capital
	# 0-255: everything
	for i in range(0,255):
		hex_byte = hex(i)[2:]

		if i <= 15:
			hex_byte = hex_byte * ciphertext_length
		else:
			hex_byte = hex_byte * int((ciphertext_length / 2))


		# Previously it was just these two lines:
			# plain = hex_xor(ciphertext,hex_byte).decode("ascii")
			# plain_list.append(plain)

		# Now, Do this check to make sure this is a valid string which can be decoded
		byte_output = hex_xor(ciphertext, hex_byte)
		bytes_valid = map(lambda x: x < 128, byte_output)		

		if not all(bytes_valid):
			pass
		else:
			plain = byte_output.decode("ascii")
			plain_list.append(plain)

	plain_list.sort(key=score_plaintext, reverse=True)
	return plain_list

# The challenge:
# print(decipher_single_byte_xor(cipher))


