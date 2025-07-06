def max_subarray_sum(arr):
    # Başlangıçta en büyük toplam ve geçici toplamı ilk elemana eşitle
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        # Yeni elemanı dahil ederken sıfırdan mı başlamalıyım, yoksa eklemeye devam mı etmeliyim?
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        print(max_ending_here)

        # Şimdiye kadar gördüğüm en büyük toplamı güncelle
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


print(max_subarray_sum([-2,11,-4,13,-5,2]))