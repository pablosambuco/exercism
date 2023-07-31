def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    if row_count == 0:
        return []

    if row_count == 1:
        return [[1]]

    salida = rows(row_count - 1)
    nivel_anterior = salida[row_count - 2]
    new_aux = []
    vueltas = row_count // 2
    extra = row_count % 2

    num1 = 0
    for i in range(vueltas+extra):
        num2 = nivel_anterior[i]
        new_aux.append(num1+num2)
        num1 = num2

    for i in range(vueltas):
        new_aux.append(new_aux[vueltas-1-i])
    salida.append(new_aux)
    return salida
