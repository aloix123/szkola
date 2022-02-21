for i in range(int(input())):
    linia=input()
    result=[]
    nie='nie'
    dllii=len(linia)
    i=0
    p=linia.find(nie,i)
    if p==-1:
        print('Brak')
    else:
        while p!=-1:

            p = linia.find(nie, i)
            result.append(p)
            i+=1
        result.remove(-1)

        print(*set(result.sort()))
