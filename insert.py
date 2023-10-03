def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

lista_numeros = [3, 1, 5, 2, 2]

insertion_sort(lista_numeros)

print("Lista ordenada:", lista_numeros)
