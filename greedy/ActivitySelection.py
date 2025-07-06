def activity_selection(activities):
    # Bitiş zamanına göre sırala
    activities.sort(key=lambda x: x[1])
    
    selected = []
    last_end_time = 0

    for activity in activities:
        start, end = activity
        if start >= last_end_time:
            selected.append(activity)
            last_end_time = end
    
    return selected

# Verilen aktiviteler
activities = [
    (10,35),
    (45,65),
    (22,70),
    (70,85),
    (75,90)
]

selected_activities = activity_selection(activities)

print("Seçilen aktiviteler:")
for i, (start, end) in enumerate(selected_activities, start=1):
    print(f"{i}. Başlangıç: {start}, Bitiş: {end}")