


"""""
CountingSort(A)
  //A[]-- Initial Array to Sort
  //Complexity: O(k)
  for i = 0 to k do
  c[i] = 0
  //Storing Count of each element
  //Complexity: O(n)
  for j = 0 to n do
  c[A[j]] = c[A[j]] + 1
  // Change C[i] such that it contains actual
  //position of these elements in output array
  ////Complexity: O(k)
  for i = 1 to k do
  c[i] = c[i] + c[i-1]
  //Build Output array from C[i]
  //Complexity: O(n)
  for j = n-1 downto 0 do
  B[ c[A[j]]-1 ] = A[j]
  c[A[j]] = c[A[j]] - 1
end func
"""
lista = [6, 9, 2, 5, 7, 9, 2, 5, 0, 1, 7, 9, 3, 1, 9, 3]
max = 1000000
pola = []
places = []
for i in range(max + 1):
    pola.append(0)
for element in lista:
    pola[element] += 1
for h in range(max):
    pola[h + 1] += pola[h]
for i in range(len(lista)):
    places.append(0)

for e in lista:
    places[pola[e] - 1] = e
    pola[e] -= 1
print(places)


