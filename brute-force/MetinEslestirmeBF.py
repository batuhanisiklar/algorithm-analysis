def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)

    # Tüm olası başlangıç pozisyonlarını deneriz
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break  # eşleşmiyorsa boşuna devam etme
        if match:
            return i  # eşleşmenin başladığı index
    return -1  # eşleşme yoksa

print(brute_force_string_match("merhaba dünya", "dünya"))  # ➜ 8