from vehiculo import Automovil

automovil_1 = Automovil("Toyota", "Yaris", 4, 120, 800)
automovil_2 = Automovil("Fiat", "Palio", 4, 95, 1200)
automovil_3 = Automovil("Ford", "Fiesta", 4, 125, 1500)
vehiculos = [automovil_1, automovil_2, automovil_3]

print("\nImprimiendo por pantalla los Vehículos:\n")
contador = 1
for vehiculo in vehiculos:
    print(f"Datos del automóvil {contador}: {vehiculo}")
    contador += 1