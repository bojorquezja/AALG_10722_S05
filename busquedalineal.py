"""
    cree un codigo que pida un 
    numero y lo busque en esta lista
    [2,5,6,8,9]
    Que avise si lo encontro o no
"""
def buslinGerson():
    buscar = int(input("Ingrese el número: "))
    encontrado = False
    op = 0
    for i in range(len(numeros)):
        op += 1
        if numeros[i] == buscar:
            print(f"El número {buscar} fue encontrado. op={op}")
            encontrado = True
            break
    if not encontrado:
        print(f"El número {buscar} NO fue encontrado. op={op}")
  
def buslinLuis():
    n = int (input("Ingresa un número para buscar: "))
    if n in numeros:
        print("El numero ha sido encontrado :>")
    else:
        print("El numero no esta en la lista :<")

numeros = [2,5,6,8,9,11,12,13,15,18,20,25,26,28,30]
buslinGerson()