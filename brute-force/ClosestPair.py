def closestPair(x,y):
    enYakinMesafe = float("inf")
    degerler = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            mesafe = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
            if mesafe < enYakinMesafe:
                enYakinMesafe = mesafe
                degerler = [(x[i],x[j]),(y[i],y[j])]
    return enYakinMesafe ,degerler

x = [2,12,40,5,12,3]
y = [3,30,50,1,10,4]

print(closestPair(x,y))