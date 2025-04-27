import math

def check_convergence(epsilon=1e-6, max_terms=100000):
    total_sum = 0
    prev_sum = None

    for k in range(1, max_terms + 1):
        term = (-1)**k / math.sqrt(k)
        term2 = 1/k**2
        total_sum += term2

        # Prüfen, ob die Differenz zwischen aufeinanderfolgenden Summen kleiner als epsilon ist
        if prev_sum is not None and abs(total_sum - prev_sum) < epsilon:
            return f"Konvergenz erreicht nach {k} Termen: {total_sum}"
        
        prev_sum = total_sum

    return f"Keine Konvergenz nach {max_terms} Termen"

# Beispielaufruf
result = check_convergence()
print(result)