def catalanNumbers(n):
    if n<0:
        return 0
    dizi = [0] * (n + 1)
    dizi[0] = 1
    dizi[1] = 1
    for i in range (2, n+1):
        for j in range (0, i):
            dizi[i] += dizi[j] * dizi[i-j-1]
    return dizi[n]

print(catalanNumbers(8))
