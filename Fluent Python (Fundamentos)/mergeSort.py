def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    mitad_izquierda = arr[:medio]
    mitad_derecha = arr[medio:]

    mitad_izquierda_ordenada = merge_sort(mitad_izquierda)
    mitad_derecha_ordenada = merge_sort(mitad_derecha)

    return merge(mitad_izquierda_ordenada, mitad_derecha_ordenada)

def merge(izquierda, derecha):
    resultado = []
    indice_izq, indice_der = 0, 0

    while indice_izq < len(izquierda) and indice_der < len(derecha):
        if izquierda[indice_izq] < derecha[indice_der]:
            resultado.append(izquierda[indice_izq])
            indice_izq += 1
        else:
            resultado.append(derecha[indice_der])
            indice_der += 1

    while indice_izq < len(izquierda):
        resultado.append(izquierda[indice_izq])
        indice_izq += 1

    while indice_der < len(derecha):
        resultado.append(derecha[indice_der])
        indice_der += 1

    return resultado