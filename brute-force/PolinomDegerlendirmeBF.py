def evaluate_polynomial(coefficients, x0):
    result = 0
    for i in range (len(coefficients)):
        result += coefficients[i] * (x0 ** i)
    return result
# Örnek: p(x) = 2x^3 + 3x^2 + 5x + 7
coeffs = [7, 5, 3, 2]  # a₀ = 7, a₁ = 5, a₂ = 3, a₃ = 2
x0 = 2

print("p(x₀) =", evaluate_polynomial(coeffs, x0))  # Çıktı: 2*8 + 3*4 + 5*2 + 7 = 16 + 12 + 10 + 7 = 45
