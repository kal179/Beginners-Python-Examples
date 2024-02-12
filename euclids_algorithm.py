# Recursive implementation of Euclidean algorithm 
def gcd(m, n):
    """
    Calculates the greatest common divisor (GCD) of two positive integers using the Euclidean algorithm.

    Args:
        m (int): First positive integer.
        n (int): Second positive integer.

    Returns:
        int: The GCD of m and n.
    """
    (a, b) = (max(m, n), min(m, n))
    while b != 0:
        a, b = b, a % b
    return a