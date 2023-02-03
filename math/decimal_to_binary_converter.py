"""
I came up with this algorithm to convert decimal(natural numbers only xd) to binary completely from scratch and 
therefore it might not be the best most efficient implementation.
Optimizations are welcome.
"""

def dec_to_bin(n):
    quo = n 
    binary = 0
    while (quo>0):
        tmp = quo
        pows = 0
        while (quo > 1):
            quo = quo // 2
            pows = pows + 1 
        quo = tmp-pow(2,pows)
        binary = binary+pow(10,pows)
    return binary

for i in range(0,101):
    print("Natural Number:"+str(i)+" Binary:"+str(dec_to_bin(i)))
