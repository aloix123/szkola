T = [21, 33, 17, 24, 31, 4, 27, 20, 18, 7]

# n - liczba elementów
# p - nr elementu początkowego
# k - nr elementu końcowego

def quicksort(p, k):
    global ile
    if p < k:
        m = p
        for i in range(p+1, k + 1):
            ile += 1
            print(ile, ")", *T)
            if T[i] < T[p]:
                m += 1
                pom = T[i]
                T[i] = T[m]
                T[m] = pom
                # print(T)
        pom = T[p]
        T[p] = T[m]
        T[m] = pom
        print(ile + 1, ")", T)

        quicksort(p, m-1)
        quicksort(m+1, k)


ile = 0
quicksort(0, len(T) - 1)
 #print(T)i} {ex_list}')