import csv
from vehiculo import *

particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
vehiculos = [particular, carga, bicicleta, motocicleta]

def guardar_datos_csv(nombre_archivo, vehiculos):
    try:
        archivo = open(nombre_archivo, "w", newline="")
        archivo_csv = csv.writer(archivo)
        for vehiculo in vehiculos:
            datos = [str(vehiculo.__class__), str(vars(vehiculo))]
            archivo_csv.writerow(datos)
    except IOError as error:
        print(f"Error al guardar en el archivo: {error}")
    finally:
        archivo.close()

def leer_datos_csv(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for tipo, atributos in archivo_csv:
            print(f"\nLista de Vehículos {tipo.split('.')[-1]}")
            print(eval(atributos))
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    except IOError as error:
        print(f"Error al leer el archivo: {error}")
    finally:
        archivo.close()

guardar_datos_csv("vehiculos.csv", vehiculos)
leer_datos_csv("vehiculos.csv")