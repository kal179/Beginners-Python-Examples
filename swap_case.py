def swap_case(s):
    swapped = ""
    for i in range(len(s)):
        temp = s[i].upper()
        if (s[i] == temp):
            swapped += s[i].lower()
        else:
            swapped += s[i].upper()
            
    return swapped    
