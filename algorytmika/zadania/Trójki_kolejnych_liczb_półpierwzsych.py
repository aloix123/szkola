
"""""to co widzisz to zadanie 'Trójki_kolejnych_liczb_półpierwzsych' , które trzeba było zrobić jako pracę domową"""""

n=input().split()


lista_liczb=[i for i in range(int(n[0]),int(n[1]))] #skrótowe napisanie listy
lista_liczb_półpierwszych=[]
for liczba in lista_liczb:
    """""algorytm , czy dana liczba jest pół-pierwsza"""""
    brr=[]#brr
    i = 2
    while  i*i<=liczba:
        """sprawdza dzielniki podanej liczby z listy"""
        if len(brr)>2:# przyśpiesza program , jeżeli jest więcej  niż  2 dzielników  to zakończ pętle
            break
        while liczba%i==0:
            liczba/=i
            brr.append(i)# karzdego dzielnika dodajemy do listy brr

        i+=1
    if liczba>1:
        brr.append(liczba)

    if len(brr)==2:
        """""dodajemy wszystkie liczby pół-pierwsze do listy finisz"""""
        lista_liczb_półpierwszych.append(brr[0] * brr[1])


        