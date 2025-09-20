"""_summary_
Haga el codigo que representa a la busqueda binaria explicada en el ppt
"""

def busBin(lista):
    op = 0
    buscar = int(input("Ingrese el número: "))
    low = 0
    hig = len(lista)-1
    while True:
        op += 1
        mid = (hig+low)//2
        if buscar < lista[mid]:
            hig = mid
        elif buscar > lista[mid]:
            low = mid
        elif buscar == lista[mid]:
            print(f"Encontrado op={op}")
            break
        
numeros = [2,5,6,8,9,11,12,13,15,18,20,25,26,28,30] 
busBin(numeros)