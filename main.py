
def encode(string, shift):
    encoded_string = ""
    string.upper()
    for char in string:
        if char.isupper():
            # find position in alphabet
            char_ord = ord(char)
            char_index = char_ord - ord("A")

            # if x-n or x+n is not in (0,25) we need to subtract or add 26
            new_index = (char_index + shift) % 26

            # convert back to letter
            new_char = chr(new_index + ord("A"))

            encoded_string += new_char
        else:
            # leave lowercase as is
            encoded_string += char
    print("Key #%s: %s" % (shift, encoded_string))

# simple brute force method
def decode (message):
    message.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # try all keys 0,25
    for key in range(len(alphabet)):
        decoded_string = ""
        for char in message:
            if char in alphabet:
                num = alphabet.find(char)
                # shift by the current key we're trying
                num -= key
                if num < 0:
                    num += len(alphabet)
                decoded_string += alphabet[num]
            else:
                decoded_string = decoded_string + char
        print("Key #%s: %s" % (key, decoded_string))

if __name__ == '__main__':
    print("ENCODING STRING \r\n")
    encode("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG OF CAESAR AND YOUR UNIQUE SOLUTION IS DHSFLIOOLEHG", 21)
    print("\r\nDECODING STRING \r\n")
    decode("OCZ LPDXF WMJRI AJS EPHKN JQZM OCZ GVUT YJB JA XVZNVM VIY TJPM PIDLPZ NJGPODJI DN YCNAGDJJGZCB")
