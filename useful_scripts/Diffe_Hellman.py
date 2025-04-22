import random, hashlib

def list_prime():
    for num in range(3, 1000):
       # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num, end=', ')

def is_prime(n):
    """if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False"""
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def cost(h, cost):
    for i in range(cost):
        h = hashlib.sha3_512(h.encode()).hexdigest()
        return h

print("type 'prime' to choose from list")
prime = input("Enter a largest prime number you can think of >>> ")
if prime == 'prime':
    list_prime()
    prime = int(input("Enter a largest prime number you can think of >>> "))
else:
    prime = int(prime)
    
if is_prime(prime):
    private = int(input("Enter your private key>>> "))
    public = random.randint(0, 999999999)
    my_share = (public**private)%prime
    my_exchange_key = cost(hashlib.sha3_512(str(my_share).encode()).hexdigest(), 5)
    print()
    print(f"Your exchange key is --> {my_exchange_key}")
    print('*' * 100)

    bob_private = int(input("Enter Bob's private key>>> "))
    bob_share = (public**private)%prime
    bob_exchange_key = cost(hashlib.sha3_512(str(bob_share).encode()).hexdigest(), 5)
    print()
    print(f"Bob'sexchange key is --> {bob_exchange_key}")
    print()
    print(f"my_exchange_key == bob_exchange_key\n{my_exchange_key == bob_exchange_key}")
    print('*' * 100)
    
else:
    print("This is not a prime number")
