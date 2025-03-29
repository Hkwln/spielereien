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


def Aks(n):
    #step 1
    for b in range(2, np.log2(n)+1):
        # n = a^b implies a = n^(1/b)
        a = n ** (1/b)
        if a ** b == n:
            return ('Composite')
    
    #step 2
    nlog = np.log2(n)**2
    for r in range(2,n ):
        #calculate ord_r until ord_r(n) > log²(n)
