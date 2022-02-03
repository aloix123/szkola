
""""" rozwiązanie zadania  'Kwadraty liczb pierwszych '"""""
# i sprawdzamy czy ta nowa liczba jest podzielna przez inne dzielniki .
# Jeżeli jest podzielna , to znaczy nie jest . A w przeciwnym wypadku jest

for i in range(int(input())):  # pętla tworząca liczbę przypadków
    num = int(input())
    n = num**0.5  # pierwiastek z num
    if n == int(n):  # sprawdzam czy liczba jest całkowita, liczba double nie jest nigdy liczbą pierwszą
        L = []
        i = 2
        while i * i <= n:
            """" sprawdzamy dzielniki liczby n"""""
            while n % i == 0:
                n /= i
                L.append(n)
            i += 1
        if n > 1:L.append(n)
        if len(L)!=1:print(n) # jeśli lista dzielników jest różna od jeden to dzielnik num (n) jest liczbą pierwszą
