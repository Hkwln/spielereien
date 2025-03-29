#aks is as well a prime number tester, without any error potential
#pseudocode from wikipedia:
#1: if n = a^b für ein b > 1 return ZUSAMMENGESETZT;
#2: r = min{ r | ordr(n) > log(n)2 };
#3: if 1 < ggT(a,n) < n für ein a ≤ r return ZUSAMMENGESETZT;
#4: if n ≤ r return PRIM;
#5: for a = 1 to sqrt(phi(r))*log(n) do
#6:     if (X+a)n ≢ Xn+a (mod (Xr−1), n) return ZUSAMMENGESETZT;
#7: return PRIM;

#Input: integer n > 1.
#1. If (n = a^b for a ∈ N and b > 1), output COMPOSITE.
#2. Find the smallest r such that or (n) > log2 n.
#3. If 1 < (a, n) < n for some a ≤ r, output COMPOSITE.
#4. If n ≤ r, output PRIME.1
#5. For a = 1 to b√φ(r) log nc do
#if ((X + a)n 6 = Xn + a (mod Xr − 1, n)), output COMPOSITE;
#6. Output PRIME;

import numpy as np
from sympy import symbols, expand
from ggt import ggt

def Aks(n):
    # Step 1
    for b in range(2, int(np.log2(n)) + 1):  # Fix range to use integers
        a = round(n ** (1 / b))  # Round to nearest integer
        if a ** b == n:
            return "COMPOSITE"

    # Step 2
    nlog = (np.log2(n)) ** 2
    for r in range(2, n):
        ktemp = 1
        for k in range(1, r + 1):  # Fix loop range
            if pow(n, k, r) == 1:  # Modular exponentiation
                ktemp = k
                break
        if ktemp > nlog:
            break  # Exit loop when condition is met

    # Step 3
    for a in range(1, r + 1):
        if 1 < ggt(a, n) < n:  # Fix condition
            return "COMPOSITE"

    # Step 4
    if n <= r:
        return "PRIME"

    # Step 5
    x = symbols('x')
    for a in range(1, int(np.sqrt(r) * np.log2(n)) + 1):  # Use np.log2 for consistency
        left = expand((x + a) ** n) % (x ** r - 1) % n  # Add modulo n
        right = (x ** n + a) % (x ** r - 1) % n  # Add modulo n
        if left != right:
            return "COMPOSITE"

    # Step 6: Output PRIME
    return "PRIME"

# Example usage
print(Aks(87))