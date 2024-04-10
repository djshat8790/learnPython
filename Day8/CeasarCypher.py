alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    cypher_text = ""
    for char in plain_text:
        if char not in alphabet:
            cypher_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > len(alphabet)-1:
                new_position = new_position - len(alphabet)
                cypher_text += alphabet[new_position]
            else:
                cypher_text += alphabet[new_position]

    print(f"Encoded word is {cypher_text}")


def decrypt(plain_text, shift_amount):
    cypher_text = ""
    for char in plain_text:
        if char not in alphabet:
            cypher_text += char
        else:
            position = alphabet.index(char)
            new_position = position - shift_amount
            if new_position < 0:
                new_position = len(alphabet) + new_position
                cypher_text += alphabet[new_position]
            else:
                cypher_text += alphabet[new_position]

    print(f"Decoded word is {cypher_text}")


def caesar(plain_text, shift_amount, function):
    cypher_text = ""
    for char in plain_text:
        if char not in alphabet:
            cypher_text += char
        elif function == "encode":
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > len(alphabet)-1:
                new_position = new_position - len(alphabet)
                cypher_text += alphabet[new_position]
            else:
                cypher_text += alphabet[new_position]
        elif function == "decode":
            position = alphabet.index(char)
            new_position = position - shift_amount
            if new_position < 0:
                new_position = len(alphabet) + new_position
                cypher_text += alphabet[new_position]
            else:
                cypher_text += alphabet[new_position]
        else:
            print("Please enter the correct direction")
            break
    if function == "encode" or function == "decode":
        print(f"{function} message is {cypher_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(plain_text=text, shift_amount=shift, function=direction)
    answer = input("Do you want to continue? Type 'Yes' or 'no'\n").lower()
    if answer == "no":
        should_continue = False
        print("Good bye!")
