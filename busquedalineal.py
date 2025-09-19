"""
    cree un codigo que pida un 
    numero y lo busque en esta lista
    [2,5,6,8,9]
    Que avise si lo encontro o no
"""
def buslinGerson():
    buscar = int(input("Ingrese el número: "))
    encontrado = False

    for i in range(len(numeros)):
        if numeros[i] == buscar:
            print(f"El número {buscar} fue encontrado.")
            encontrado = True
            break
    if not encontrado:
        print(f"El número {buscar} NO fue encontrado.")
  
def buslinLuis():
    n = int (input("Ingresa un número para buscar: "))
    if n in numeros:
        print("El numero ha sido encontrado :>")
    else:
        print("El numero no esta en la lista :<")

numeros = [6, 5, 2, 8, 9]  
buslinLuis()