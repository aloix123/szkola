
""""" rozwiązanie zadania  'Kwadraty liczb pierwszych '"""""
# Drógi sposób rozwiązania zadania polega na zprawdzeniu dzielników .
# danej liczby i sprawdzić czy są tylko dwa i , czy są sobie równe.
for i in range(int(input())): # pętla ,
    liczba=int(input())
    brr=[]# lista , która przechowuje dzielniki danej liczby
    i = 2
    while  i*i<=liczba:
        """ wyznaczam dzielniki podanej liczby"""
        while liczba%i==0:
            liczba/=i
            brr.append(i)
        i+=1
    if liczba>1:
        brr.append(liczba)
    # sprawdzam tutaj , czy liczba dzielników wynosi 2 i czy te liczby są sobie równe
    if len(brr)==2 and brr[0]==brr[1]:
        print(brr[0]*brr[1])
