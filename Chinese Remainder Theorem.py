def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1  # If no modular inverse exists

def chinese_remainder_theorem(n, a):
    # Calculate the product of all moduli
    N = 1
    for ni in n:
        N *= ni

    # Compute the solution
    result = 0
    for i in range(len(n)):
        Ni = N // n[i]  # Product of all moduli except the current one
        inv = mod_inverse(Ni, n[i])
        if inv == -1:
            print(f"No modular inverse found for Ni = {Ni}, mod = {n[i]}")
            return -1
        print(f"Step {i+1}: Ni = {Ni}, inv = {inv}, ai = {a[i]}, adding {a[i]} * {Ni} * {inv}")
        result += a[i] * Ni * inv

    # Final result modulo N
    return result % N

# Input: Moduli and Remainders
print("Chinese Remainder Theorem")
k = int(input("Enter the number of equations: "))

n = []
a = []

print("Enter the moduli (n1, n2, ..., nk):")
for i in range(k):
    n.append(int(input(f"n{i+1}: ")))

print("Enter the remainders (a1, a2, ..., ak):")
for i in range(k):
    a.append(int(input(f"a{i+1}: ")))

# Calculate and display the result
result = chinese_remainder_theorem(n, a)
if result != -1:
    print(f"\nThe solution to the system of congruences is x = {result}")
