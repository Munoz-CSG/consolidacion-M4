from dataclasses import dataclass

@dataclass
class Vehiculo:
    marca: str
    modelo: str
    __num_ruedas: int

    @property
    def num_ruedas(self):
        return self.__num_ruedas

    @num_ruedas.setter
    def num_ruedas(self, nueva_num_ruedas):
        if nueva_num_ruedas < 0:
            raise ValueError("Error: Sea serio, su número de ruedas no puede ser negativo.")
        self.__num_ruedas = nueva_num_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"

@dataclass
class Automovil(Vehiculo):
    __velocidad: int
    __cilindrada: int

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        if nueva_velocidad < 0:
            raise ValueError("Error: Sea serio, su velocidad no puede ser negativa.")
        self.__velocidad = nueva_velocidad

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, nueva_cilindrada):
        if nueva_cilindrada <= 0:
            raise ValueError("Error: Sea serio, su cilindrada debe ser mayor que 0.")
        self.__cilindrada = nueva_cilindrada

    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc"

@dataclass
class Particular(Automovil):
    __puestos: int

    @property
    def puestos(self):
        return self.__puestos

    @puestos.setter
    def puestos(self, nuevo_puestos):
        if nuevo_puestos <= 0:
            raise ValueError("Error: Sea serio, su número de puestos puede ser mayor que 0.")
        self.__puestos = nuevo_puestos

    def __str__(self):
        return f"{super().__str__()}, Puestos: {self.puestos}"

@dataclass
class Carga(Automovil):
    __carga: float

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, valor):
        if valor < 0:
            raise ValueError("Error: Sea serio, su carga no puede ser negativa.")
        self.__carga = valor

    def __str__(self):
        return f"{super().__str__()}, Carga: {self.carga} Kg"

@dataclass
class Bicicleta(Vehiculo):
    __tipo: str

    def __post_init__(self):
        self.tipo = self.__tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        if tipo not in ["Urbana", "Carrera", "Deportiva"]:
            raise ValueError("Error: El tipo de bicicleta solo puede ser 'Urbana' o 'Carrera'.")
        self.__tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"

@dataclass
class Motocicleta(Bicicleta):
    motor: str
    cuadro: str
    __num_radios: int

    @property
    def num_radios(self):
        return self.__num_radios

    @num_radios.setter
    def num_radios(self, nueva_num_radios):
        if nueva_num_radios < 0:
            raise ValueError("Error: Su número de radios no puede ser negativo.")
        self.__num_radios = nueva_num_radios

    def __str__(self):
        return f"{super().__str__()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.num_radios}"