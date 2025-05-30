import datetime
from centros_salud import CentrosSalud



class Pacientes: 
    """
    Esta clase (padre) contiene la informacion sobre los pacientes 
    """

    def __init__(self, DNI: int, nombre: str, fecha_nacimiento: datetime, sexo: str, telefono: int, sangre: str, centro_salud_asociado: CentrosSalud):
        self.dni = DNI
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.sangre = sangre
        self.centro_salud = centro_salud_asociado
        pass

    def __str__(self):
        return f"{self.nombre}" 