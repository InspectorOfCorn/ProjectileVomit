import string
plain_text = "cool seeing you here"
shift = 7
#shift = 7 is the cipher, to decipher take total of characters and subtract by shift.
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
#Line 7 shows alphabet and shifted alphabet on a table stacked where individual characters can become graphed
encrypted = plain_text.translate(table)
print(encrypted)

#We will build more structure below, Second Code allows for more Leeway with different characters aka. Punct, Capital, Symbols
def caeser(text, shift, alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    shifted_alphabet = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabet)
    table2 = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table2)

plain_text2 = "Throw rocks at homeless people for free cash."
print(caeser(plain_text2, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
