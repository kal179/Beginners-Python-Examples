# binary_to_decimal.py
#
# Description: A program to convert binary string(s) to decimal. Test case included for testing purposes.
#
# Author: Chaitanya Mittal
# Date: 2023-11-17 10:14:20.288913

"""Idea:
- def a function to decode 1 byte:
    - get the list
    - get value by multiplying each element with 2** its index from reverse (pattern observation)
      .... (instead of this we can multiply index to list reversed)......
    - return the sum of value

- get input
- split it to get rid of spaces (assume user is well behaved and will enter 1-space separated string only)
- convert each byte and compile result in a list
- print the converted bytes separated by space
"""


def byte_decode(binary):
    # Convert binary string to list
    lst = list(binary)[::-1]
    
    # Initialize variables
    length = len(binary)
    sum = 0
    
    # Loop through each character in the binary string
    for i in range(length):
        # Calculate value of each bit
        value = int(lst[i]) * (2 ** i)
        
        # Add value to the sum
        sum += value
    
    # Return the final sum
    return sum

#  ____ Main Program  ____ #

# Get input of the required binary string
binary = input("Binary: ").split(" ")
"""  TESTING PURPOSES
string = ("01010101 01101110 01100100 01100101 0110010 00100000 01011001 01101111 01110101 01110010 00100000 01010011 01100101 01100001 01110100").split()
binary = list(string)"""

# Initialize an empty list to store 'evaluated' bytes
bytes_translated = list()
#translate the byte and append it to the list
for byte in binary:
    bytes_translated.append(byte_decode(byte))

# Print the output
print(f'Evaluated: ', end = "")
for byte in bytes_translated:
    print(byte, end = " ")
print()


        
