def radix_sort_with_buckets(arr):
    if len(arr) == 0:
        return arr

    # En büyük elemanı bul
    max_num = max(arr)
    exp = 1  # Basamak (1'ler, 10'lar, 100'ler)

    while max_num // exp > 0:
        # Her basamak için 10 tane bucket oluştur (0-9 arası)
        buckets = [[] for _ in range(10)]

        # Sayıları ilgili bucket'a yerleştir
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        # Bucket'ları sırayla birleştir
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        # Sonraki basamağa geç
        exp *= 10

    return arr

# Örnek kullanım
dizi = [170, 45, 75, 90, 802, 24, 2, 66]
sirali_dizi = radix_sort_with_buckets(dizi)
print("Sıralı Dizi:", sirali_dizi)