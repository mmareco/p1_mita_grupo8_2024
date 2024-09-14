import random

def crear_matriz(num_estudiantes, num_materias):
    matriz = []
    for i in range(num_estudiantes):
        fila = []
        for j in range(num_materias):
            calificacion = random.randint(1, 10)  
            fila.append(calificacion) 
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz, estudiantes, materias):
    print("       ", end="")
    for materia in materias:
        print(f"{materia} ", end="")
    print()
    
    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]:<10}", end="")  #imprime el nombre del estudiante alineado a la izquierda, ocupando al menos 10 caracteres de ancho
        for j in range(len(materias)):
            print(f"{matriz[i][j]:<10}", end="")  
        print()

def calcular_promedio_estudiantes(matriz, estudiantes):
    print("\nPromedio por Estudiante:")
    for i in range(len(estudiantes)):
        suma = sum(matriz[i])  
        promedio = suma / len(matriz[i]) 
        print(f"{estudiantes[i]}: {promedio:.2f}")

def calcular_promedio_materias(matriz, materias):
    print("\nPromedio por Materia:")
    for j in range(len(materias)):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]  
        promedio = suma / len(matriz)  
        print(f"{materias[j]}: {promedio:.2f}")

def main():
    estudiantes = ["Juan", "Maria", "Luis", "Ana"]
    materias = ["Matemáticas", "Física", "Química", "Historia"]
    
    matriz = crear_matriz(len(estudiantes), len(materias))
    
    mostrar_matriz(matriz, estudiantes, materias)
    
    calcular_promedio_estudiantes(matriz, estudiantes)
    
    calcular_promedio_materias(matriz, materias)

main()
