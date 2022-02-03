
ex_list=[21,33,17,24,31,4,27,20,18,7]
21












i=0
flaga=True

while i<len(ex_list)-1 and flaga:
    j=0
    flaga=False
    while j<len(ex_list)-1-i:
        if ex_list[j]>ex_list[j+1]:
            ex_list[j],ex_list[j+1]=ex_list[j+1],ex_list[j]

            flaga=True
        j += 1
    i+=1
    print(ex_list)
"""""
Dane:
ex_lista[0,1..]
Wynik:
posortowane ex_lista[0,1..]
i->0
bulin->Prawda
g->długość_listy(ex_lista)
Dopuki i<g -1  oraz bulin wykonaj:
    j->0
    bulin->Fałsz
    Dopuki j<g-i-1 wykonaj:
        Jeśli ex_lista[j]>ex_lista[j+1:
            p->ex_lista[j]
            ex-lista[j]->T[j+1]
            T[j+1]->p
            bulin->Prawda
        j->j+1
        
    i->i+1
"""
