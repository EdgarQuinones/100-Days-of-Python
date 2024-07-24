alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        for index in range(len(alphabet)):
            if alphabet[index] == letter:
                shift_number = index + shift
                new_letter = alphabet[shift_number]
                if shift_number > 25:
                    extra = shift_number - 25
                    new_letter = alphabet[extra]
                encrypted_text += new_letter
    print(f"Encrypted Message: {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        for index in range(len(alphabet)):
            if alphabet[index] == letter:
                shift_number = index - shift
                new_letter = alphabet[shift_number]
                if shift_number < 0:
                    extra = 25 + shift_number
                    new_letter = alphabet[extra]
                decrypted_text += new_letter
    print(f"Encrypted Message: {decrypted_text}")

program_ended = False
while not program_ended:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    again = input("Again? y/n: ").lower()

    if again == "n":
        program_ended = True
