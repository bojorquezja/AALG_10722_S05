def ordsel(lista):
    for manoIzq in range(len(lista)-2):
        posMen = manoIzq
        for vista in range(manoIzq+1, len(lista)):
            if lista[vista] < lista[posMen]:
                posMen = vista
        lista[manoIzq], lista[posMen] = lista[posMen], lista[manoIzq]


numeros = [12, 11, 13, 15, 6, 9, 30, 26, 28, 18, 8, 2, 20, 5, 25]
ordsel(numeros)
print(numeros)
