def trenIstasyon(arrivals, departures):
    n = len(arrivals)
    arrivals.sort()
    departures.sort()
    platform = 0
    max_platform = 0
    i = 0
    j = 0
    while i < n and j < n:
        if arrivals[i] < departures[j]:
            platform += 1
            if platform > max_platform:
                max_platform = platform
            i += 1
        else:
            platform -= 1
            j += 1

    return max_platform
arrivals  = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]

print(trenIstasyon(arrivals, departures))  # Çıktı: 3
