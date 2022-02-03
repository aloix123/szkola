


def prawoskrętny(num):
    macierz=[]

    square=-num*2
    for i in range(square):
        macierz.append([])
    for g in macierz:
        for i in range(square):
            g.append(".")

    #leftup
    e=0
    g=int(len(macierz)/2)
    y=0
    while e<int(len(macierz)/2) :
        for i in range(y,g):

            macierz[e][i]="*"
        e+=1

        y+=1
    #rightup
    f=1
    d=0
    while f<int(len(macierz)/2)+1 and d<int(len(macierz)/2):
        for i in range(1,f+1):

            macierz[d][-i]="*"

        f+= 1
        d+=1
    #leftdown
    g=int(len(macierz)/2)
    q=int(len(macierz)/2)
    y=0
    while q>0:
        for i in range(0,q):

            macierz[-q][i]="*"
        q-=1
    # rightdown
    e=-1
    g=int(len(macierz)/2)
    stala=int(len(macierz)/2)
    while e>-int(len(macierz)/2)-1 :
        for i in range(g):

            macierz[e][stala+i]="*"
        e-=1
        g-=1


    converter(macierz)
def lewoskrętny(num):
    macierz=[]

    square=num*2
    for i in range(square):
        macierz.append([])
    for g in macierz:
        for i in range(square):
            g.append(".")


    e=0
    #leftup
    while e< (int(len(macierz)/2)):
        for i in range(e+1):
            macierz[e][i]="*"
        e += 1
    #rightup
    f=int(len(macierz)/2)
    d=0
    while f>0 and d<int(len(macierz)):
        for i in range(f):

            macierz[d][int(len(macierz)/2)+i]="*"

        f-= 1
        d+=1
    #leftdown
    g=int(len(macierz)/2)
    q=-1
    y=0
    while q>-int(len(macierz)) and y<g:
        for i in range(y,g):

            macierz[q][i]="*"
        q-=1

        y+=1
    e=-1
    g=1
    #rightdown
    while e>-int(len(macierz)/2)-1 :
        for i in range(1,g+1):

            macierz[e][-i]="*"
        e-=1
        g+=1
    converter(macierz)


def converter(list):
    finalstring=[]

    for element in list:
        string = ''
        for e in element:
            string+=e
        finalstring.append(string)
    for i in finalstring:
        print(i)

while True:
    parametr=int(input())
    if parametr>0:
        lewoskrętny(parametr)
    elif parametr<0:
        prawoskrętny(parametr)
    elif parametr==0:
        break

























# potęgi 2 24862486