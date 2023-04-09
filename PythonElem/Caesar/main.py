import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

running = True


def caesar(text1, shift1, direction1):
#Declare empty variable
    cipher = ""
#Check Input
    if direction1 == "encode":
#Iterate through each letter in the message
        for char in text1:
#Checks to see if each character is in the alphabet list.  If true continues else it skips and appends it to cipher string
            if char in alphabet:
#Create a cipher index using alphabet list and increasing by shift input
                cipher_index = alphabet.index(char) + shift1
#Add the new letters to the cipher variable by checking the cipher index with the alphabet list
                cipher += alphabet[cipher_index % 26]
            else:
                cipher += char
    elif direction1 == "decode":
        for char in text1:
            if char in alphabet:
                cipher_index = alphabet.index(char) - shift1
                cipher += alphabet[cipher_index % 26]
            else:
                cipher += char

#Output
    print(f"Your original word is: {text1}")
    print(f"Your {direction1}d word is: {cipher}")


while running:
    print(art.logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text1=text, shift1=shift, direction1=direction)

    cont = input("\n\nWould you like to continue?: ").lower()
    if cont == "y" or cont == "yes":
        continue
    else:
        break
