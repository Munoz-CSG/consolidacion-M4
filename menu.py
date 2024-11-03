import os
def ejecutar_sprint(sprint):
    os.system(f"python {sprint}.py")

def mostrar_menu():
    while True:
        print("\nSeleccione el SPRINT que desea ejecutar:")
        print("1. Sprint 1")
        print("2. Sprint 2")
        print("3. Sprint 3")
        print("4. Salir")
        opcion = input("Ingrese el número del sprint que desea ejecutar (Entre 1 y 3): ")

        if opcion == "1":
            ejecutar_sprint('sprint_1')
        elif opcion == "2":
            ejecutar_sprint('sprint_2')
        elif opcion == "3":
            ejecutar_sprint('sprint_3')
        elif opcion == "4":
            print("Gracias. Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")
            
mostrar_menu()