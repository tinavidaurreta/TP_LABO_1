from especialista import Especialista
from generales import Generales
from auto import Auto
from helicoptero import Helicoptero
from avion import Avion


class centrosSalud:

    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str, telefono: int, lista_cirujanos:list[Generales | Especialista], lista_vehiculos: list[ Helicoptero | Auto| Avion]):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia 
        self.telefono = telefono
        self.lista_cirujanos = lista_cirujanos
        self.lista_vehiculos = lista_vehiculos
        pass