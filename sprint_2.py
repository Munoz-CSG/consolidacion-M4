from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
vehiculos = [particular, carga, bicicleta, motocicleta]

print("\nImprimiendo por pantalla los Vehículos:\n")
contador = 1
for vehiculo in vehiculos:
    print(f"Datos vehículo {contador}: {vehiculo}")
    contador += 1

print(f"\nMotocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")