import string 

def concat_elements(n):
    res = ""
    for i in n:
        res += i 
    return res

def encrypt(message, key):
    string_chars = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits) + list(string.punctuation) + [" "]
    try:
        splitted_message = list(message)
    except TypeError:
        return "Expected an string for message!"
        
    for char in splitted_message:
        try:
            tmp = string_chars[string_chars.index(char) + key]
        except IndexError:
            tmp_key = (string_chars.index(char) + key) -  len(string_chars)
            tmp = string_chars[tmp_key]
        splitted_message[splitted_message.index(char)] = tmp
        
    final = concat_elements(splitted_message)
    return final 
    
def n_encrypt(ciph, key, times):
    # You can modify this to take multiple keys
    i = 0
    ciph = ""
    while i < times:
        ciph = encrypt(ciph, key)
        i += 1
    return ciph
        

# Test
mesage = "This is top secret!"
result = encrypt(mesage, 9)
print("Encrypted Text: " + result)
