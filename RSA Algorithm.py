import random
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    return primes

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def power_mod(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

def rsa():
    # Generate primes
    primes = generate_primes(100)
    p = random.choice(primes)
    q = random.choice(primes)
    while p == q:
        q = random.choice(primes)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Compute d (modular multiplicative inverse of e mod phi)
    d = mod_inverse(e, phi)

    print(f"Selected primes: p = {p}, q = {q}")
    print(f"n = {n}")
    print(f"phi(n) = {phi}")
    print(f"Public key: (e = {e}, n = {n})")
    print(f"Private key: (d = {d}, n = {n})")

    # Encryption
    message = int(input("\nEnter the message (an integer less than n): "))
    if message >= n:
        print(f"Message should be less than {n}")
        return

    print(f"\n--- Encryption Process ---")
    print(f"Calculating c = m^e mod n: c = {message}^{e} mod {n}")
    c = power_mod(message, e, n)
    print(f"Encrypted message: {c}")

    # Decryption
    print(f"\n--- Decryption Process ---")
    print(f"Calculating m = c^d mod n: m = {c}^{d} mod {n}")
    decrypted_message = power_mod(c, d, n)
    print(f"Decrypted message: {decrypted_message}")

# Run the RSA algorithm
rsa()
