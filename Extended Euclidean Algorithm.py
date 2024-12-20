def extended_gcd(a, b):
    if b == 0:
        print(f"\nBase case: {a} * 1 + {b} * 0 = {a}\n")
        return a, 1, 0

    print(f"Recursing with a = {a}, b = {b}")
    gcd, x1, y1 = extended_gcd(b, a % b)

    # Compute current x and y using the results of recursion
    x = y1
    y = x1 - (a // b) * y1

    print(f"Backtracking step: {a} * {x} + {b} * {y} = {a} * {x1} + {b} * ({y1} - ({a} // {b}) * {y1}) = {gcd}")
    return gcd, x, y

def main():
    print("Extended Euclidean Algorithm Implementation")
    a = int(input("Enter first integer (a): "))
    b = int(input("Enter second integer (b): "))

    gcd, x, y = extended_gcd(a, b)

    print(f"\nGCD of {a} and {b} is: {gcd}")
    print(f"Coefficients x and y are: x = {x}, y = {y}")
    print(f"Verification: {a} * ({x}) + {b} * ({y}) = {gcd}")

if __name__ == "__main__":
    main()
