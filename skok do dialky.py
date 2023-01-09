subor1 = open('skok_do_dialky.txt','r')

krajiny = []
pocet = []
kp = []
mena = []
skoky = []
naj = 0
p = 0
ii = 0
najlepsi=[]
for riadok in subor1:
    riadok = riadok.strip()
    riadok = riadok.split()
    krajiny.append(riadok[1])
    mena.append(riadok[0])
    skoky.append(riadok[2:])
kp = [*set(krajiny)]

for krajina in kp:
    pocet.append(krajiny.count(krajina))
    
print('Účastníci sú z krajín:', kp)

for i in range(len(kp)):
    print('Počet súťažiacich z',kp[i],'je',pocet[i])

for i in skoky:
    p += 1
    for j in range(5):
        if int(i[j]) > naj:
            naj = int(i[j])
            ii = p-1
najlepsi.append(mena[ii])
p = 0
for i in skoky:
    p += 1
    for j in range(5):
        if (int(i[j]) == naj) and (mena[p-1] not in najlepsi):
            najlepsi.append(mena[p-1])
            
print('Najďalej skočil',najlepsi)

            

