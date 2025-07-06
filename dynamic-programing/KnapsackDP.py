def knapsack(values, weights, capacity):
    n = len(values)  # Toplam eşya sayısı

    # DinamikProgramlama tablosu oluşturuluyor: satırlar eşyalar, sütunlar kapasite
    # dp[i][w]: ilk i eşyadan, toplam kapasite w ile elde edilebilecek maksimum değer
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # DinamikProgramlama tablosunu doldur
    for i in range(1, n + 1):  # Her eşya için
        for w in range(capacity + 1):  # Her kapasite değeri için
            if weights[i - 1] <= w:
                # Eşyayı alma kararı:
                # max(almamak, almak)
                dp[i][w] = max(
                    dp[i - 1][w],  # Bu eşyayı almıyoruz
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]  # Alıyoruz
                )
            else:
                # Bu eşyayı alamayız, kapasite yetmiyor
                dp[i][w] = dp[i - 1][w]

    # Maksimum değer dp[n][capacity] hücresinde
    max_value = dp[n][capacity]

    # Şimdi seçilen eşyaları geri izleme ile bulalım
    selected_items = []
    w = capacity

    # Eşyaları tersten inceleyerek seçilenleri bul
    for i in range(n, 0, -1):
        # Eğer bu eşya alınmışsa, bir önceki değerle aynı olmayacaktır
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # Eşya i-1 seçilmiş
            w -= weights[i - 1]  # Kapasiteden bu eşyanın ağırlığını çıkar

    # Sonuçları döndür
    return max_value, selected_items

values = [175, 90, 20, 50, 10, 200]
weights = [10, 9, 4, 2, 1, 20]
capacity = 20

print(knapsack(values, weights, capacity))  # Çıktı: 220
