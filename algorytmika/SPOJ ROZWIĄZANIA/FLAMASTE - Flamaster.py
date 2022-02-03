for i in range(int(input())):
    waz = input();listwaz = []
    for l in range(len(waz)): listwaz.append(waz[l])
    final: str = '';i = 0
    while i < len(listwaz):
        k = 0
        try:
            while i < len(listwaz) and listwaz[i] == listwaz[i + 1]:
                k += 1;i += 1
        except: pass
        if k >= 2:final += listwaz[i] + str(k + 1)
        elif k == 1:final += listwaz[i] + listwaz[i]
        else:final += listwaz[i]
        i += 1
    print(final)
