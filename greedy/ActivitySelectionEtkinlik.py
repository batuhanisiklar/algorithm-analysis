def etkinlikSecim(start,end):
    secilenlerBaslangic = []
    secilenlerBitis = []
    sonEtkinlikBitis = 0
    for i in range(len(start)):
        if sonEtkinlikBitis < start[i]:
            secilenlerBaslangic.append(start[i])
            secilenlerBitis.append(end[i])
            sonEtkinlikBitis = end[i]
    return secilenlerBaslangic,secilenlerBitis

start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]

print(etkinlikSecim(start,end))