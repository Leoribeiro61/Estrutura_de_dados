def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Criar a lista
lista_numeros = [3, 1, 5, 2, 2]

# Aplicar o Selection Sort na lista
selection_sort(lista_numeros)

# Imprimir a lista ordenada
print("Lista ordenada:", lista_numeros)
