'''
¿Cómo podrías definir una matriz con dimensiones dadas por el usuario y permitir que además ingrese los valores de cada elemento?
'''

def crear_matriz(ff, cc):
    matriz = [[0] * cc for fila in range(ff)]
    return matriz

def cargar_datos(ff, cc, mm):
    for filas in range(ff):
        for columnas in range(cc):
            dato = int(input(f'Ingrese el dato que quiere colocar en la fila {filas} columna {columnas}: '))
            mm[filas][columnas] = dato
    print(mm)

def main():
    filas = int(input('Ingrese la cantidad de filas: '))
    columnas = int(input('Ingrese la cantidad de columnas: '))
    
    matriz = crear_matriz(filas, columnas)
    cargar_datos(filas, columnas, matriz)
    
main()
