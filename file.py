mangchuacacdoi=[[1,3,0,0],[3,3,3,1],[3,1,1,3]]
mangchuasodoi=[]
tranthang=0
tranthua=0
tranhoa=0
tongdiem=0
i=0
e=0
for f in range(len(mangchuacacdoi)):
    mangchuasodoi.append([])
print(mangchuasodoi)
while i <len(mangchuacacdoi):
    while e < len(mangchuacacdoi[i]):
        if mangchuacacdoi[i][e]==1:
            tranhoa+=1
        elif mangchuacacdoi[i][e]==3:
            tranthang+=1
        elif mangchuacacdoi[i][e]==0:
            tranthua+=1
        e+=1
    e=0
    mangchuasodoi[i].append(tranthang)
    mangchuasodoi[i].append(tranhoa)
    mangchuasodoi[i].append(tranthua)
    mangchuasodoi[i].append(tranthang*3+tranhoa*1)
    tranthang=0
    tranthua=0
    tranhoa=0
    tongdiem=0
    i+=1
print(mangchuasodoi)
z=0
k=0
while z <len(mangchuasodoi):
    while k < len(mangchuasodoi[z]) :
        if k == (len(mangchuasodoi[z])-1):
             print (mangchuasodoi[z][k])
             print("")
        else:
             print(mangchuasodoi[z][k],"",end='')
        k+=1
    k=0
    z+=1
manglonnhat=max(mangchuasodoi)
soh=0
while soh < len(mangchuasodoi) :
    if mangchuasodoi[soh] == manglonnhat:
         print(soh+1)
    soh+=1
