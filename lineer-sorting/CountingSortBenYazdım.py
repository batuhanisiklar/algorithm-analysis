def countingSort(arr):
    max_val = max(arr)
    bos_array = [0] * (max_val + 1)
    for i in arr:
        bos_array[i] += 1
    print(bos_array)
    sirali_dizi = []
    for i in range(len(bos_array)):
        if bos_array[i] != 0:
            for j in range(bos_array[i]):
                sirali_dizi.append(i)
    return sirali_dizi

# Örnek kullanım
dizi = [4, 2, 2, 8, 3, 3, 1]
sirali_dizi = countingSort(dizi)
print("Sıralı Dizi:", sirali_dizi)