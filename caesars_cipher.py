
def concat_elements(n):
    res = ""
    for i in n:
        res += i 
    return res

def encrypt(message, key):
    if key > 26:
        return "Invalid argument for key!"
    try:
        splitted_message = list(message)
    except TypeError:
        return "Expected an string for message!"
    for char in splitted_message:
        tmp = chr(ord(char) + key)
        splitted_message[splitted_message.index(char)] = tmp
        
    final = concat_elements(splitted_message)
    return final 
    
def n_encrypt(ciph, key, times):
    # You can modify this to take multiple keys
    i = 0
    while i < times:
        ciph = encrypt(ciph, key)
        i += 1
    return ciph
        

# Test
mesage = "Hey there how are you?"
result = encrypt(mesage, 9)
print("Encrypted Message: " + result)
