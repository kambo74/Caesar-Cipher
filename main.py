alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'Encode' to encode, type 'Decode' to decode: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(original_text, shift_amount):
	cipher_text = ""
	for letter in original_text:
		shifted_index = alphabets.index(letter)+ shift_amount
		shifted_index %= len(alphabets)                              # handles index out of bounds
		cipher_text += alphabets[shifted_index ]
	print(cipher_text)

encrypt(text, shift)



