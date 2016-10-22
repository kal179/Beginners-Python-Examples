getToEncrypt = str(input('Message to encrypt : '))  # string to encrypt
key = int(input('Key for encryption : '))   # key of cipher for encryption

def cipher(message):
    for x in message:
            prepare = ord(x) # returns ascii value of character
            prepareMore = chr(prepare + key)  # chr() returns character from ascii value
            return(str(prepareMore)) # returning value

final = list(map(cipher, getToEncrypt))     # converting message into list of elements

def concatenateElements(dogs):
    result= ''
    for element in dogs:
        result += str(element)
    return('Encrypted message is :  ' + result) # unpacking list and concatenating its elements

print(concatenateElements(final)) # printing elements
