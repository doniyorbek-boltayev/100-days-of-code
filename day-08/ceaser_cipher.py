from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Enter your message: ").lower()
shift = int(input("Enter the shift number: "))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    original_text = original_text.lower()
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            position = alphabet.index(letter) + shift_amount
            position %= len(alphabet)
            cipher_text += alphabet[position]
    print(f"Here is encoded text: {cipher_text}")

def decrypt(origianl_text, shift_amount):
    plain_text = ""
    origianl_text = origianl_text.lower()
    for letter in origianl_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            position = alphabet.index(letter) - shift_amount
            position %= len(alphabet)
            plain_text += alphabet[position]
    print(f"Here is decoded text {plain_text}")

def caesar(choice, original_text, shift_amount):
    if choice == "encode":
        encrypt(original_text, shift_amount)
    elif choice == "decode":
        decrypt(original_text, shift_amount)
    else:
        print("Invalid input! Try again")
game_is_on = True
while game_is_on:
    caesar(choice=direction, original_text=text, shift_amount=shift)
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if user_input == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        text = input("Enter your message: ").lower()
        shift = int(input("Enter the shift number: "))
    else:
        print("Goodbye")
        game_is_on = False
