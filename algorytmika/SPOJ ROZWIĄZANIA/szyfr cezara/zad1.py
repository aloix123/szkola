file = open('dane_6_1.txt', 'r')  # r do odczytu
A = file.readlines()

k=107
k=k%26

for slowo in A:
    nie = []
    haha=[]

    for litera in slowo:

        haha.append(litera)
    for x in haha:

        nie.append(ord(x))
    nie = list(map(lambda x: x + k, nie))
    nie = list(map(lambda x: chr(x), nie))
    result=""
    for r in nie:
        result+=r
    print("slowo: "+slowo+" przerowbiono na "+result)





