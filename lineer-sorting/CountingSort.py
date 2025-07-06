def counting_sort(arr):
    if not arr:
        return []

    # 1. Maksimum değeri bul
    max_val = max(arr)
    print(max_val)
    # 2. Count dizisini oluştur
    count = [0] * (max_val + 1)
    print(count)

    # 3. Her elemanı say
    for num in arr:
        count[num] += 1
        print(count)

    # 4. Sıralı diziyi oluştur
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
        print(sorted_arr)

    return sorted_arr

# Örnek kullanım
dizi = [4, 2, 2, 8, 3, 3, 1]
sirali_dizi = counting_sort(dizi)
print("Sıralı Dizi:", sirali_dizi)
