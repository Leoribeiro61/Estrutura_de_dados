def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

lista_numeros = [3, 1, 5, 2, 2]

bubble_sort(lista_numeros)

print("Lista ordenada:", lista_numeros)
