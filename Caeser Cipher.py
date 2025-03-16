alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again=""
while again.lower() == "yes" or again == "":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = list(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))


    def encrypt(original_text, shift_amount, dir):
        coded = ""
        if dir == "decode":
            shift_amount = shift_amount*(-1)
        for letter in original_text:
            if letter in alphabet:
                shifted_index = (alphabet.index(letter)+shift_amount)%26
                coded += alphabet[shifted_index]

            else:
                coded+=letter
        if direction=="encode":
            print(f"Your encrypted text is:\n{coded}")
        if direction=="decode":
            print(f"Your decrypted text is:\n{coded}")



    encrypt(text, shift, direction)
    again = input("\nType 'yes' if you want to go again. Otherwise, type 'no': ").strip().lower()
    if again == "no":
        print("Goodbye")