from art import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
game_over = False

while not game_over :
	direction = input("Type 'Encode' to encode, type 'Decode' to decode: ").lower()
	text = input("Type your message: ").lower()
	shift = int(input("Type the shift number: "))



	def caesar(encode_or_decode, original_text, shift_amount):
		if encode_or_decode == 'encode':
			cipher_text = ""
			for letter in original_text:
				shifted_index = alphabets.index(letter) + shift_amount
				shifted_index %= len(alphabets)  # handles index out of bounds
				cipher_text += alphabets[shifted_index]
			print(cipher_text)

		elif encode_or_decode == 'decode':
			cipher_text = ""
			for letter in original_text:
				shifted_index = alphabets.index(letter) - shift_amount
				shifted_index %= len(alphabets)
				cipher_text += alphabets[shifted_index]
			print(cipher_text)

	caesar(direction, text, shift)
	if "no" == input("You want go again? type 'yes' or 'no'.\n").lower():
		game_over = True