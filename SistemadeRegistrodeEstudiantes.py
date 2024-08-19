estudiantes = {}

def agregar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    notas = []
    while True:
        entrada = input("Ingresa una nota (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    estudiantes[nombre] = notas
    print(f"Estudiante {nombre} agregado con éxito!")

def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return
    
    print("Estudiantes registrados:")
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas) if len(notas) > 0 else 0
        print(f"{nombre}: {notas} (Promedio: {promedio})")
        
def promedio_general():
    total_notas = 0
    total_estudiantes = 0
    for notas in estudiantes.values():
        total_notas += sum(notas)
        total_estudiantes += len(notas)
    
    if total_estudiantes == 0:
        return 0
    
    return total_notas / total_estudiantes

def buscar_estudiante():
    nombre = input("Ingresa el nombre del estudiante que deseas buscar: ")
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        promedio = sum(notas) / len(notas) if len(notas) > 0 else 0
        print(f"{nombre}: {notas} (Promedio: {promedio})")
    else:
        print(f"El estudiante {nombre} no está registrado.")

def actualizar_calificaciones():
    nombre = input("Ingresa el nombre del estudiante cuya calificación deseas actualizar: ")
    if nombre in estudiantes:
        notas = []
        while True:
            entrada = input("Ingresa una nueva nota (o escribe 'fin' para terminar): ")
            if entrada.lower() == 'fin':
                break
            try:
                nota = float(entrada)
                notas.append(nota)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        estudiantes[nombre] = notas
        print(f"Las calificaciones del estudiante {nombre} han sido actualizadas.")
    else:
        print(f"El estudiante {nombre} no está registrado.")

def main():
    while True:
        print("\nMenú del Sistema de Registro")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Mostrar promedio general")
        print("4. Buscar estudiante")
        print("5. Actualizar calificaciones")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            promedio = promedio_general()
            print(f"El promedio general de todas las calificaciones es: {promedio}")
        elif opcion == '4':
            buscar_estudiante()
        elif opcion == '5':
            actualizar_calificaciones()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

main()
