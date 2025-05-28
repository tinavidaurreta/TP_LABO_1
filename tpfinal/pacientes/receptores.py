from tpfinal.pacientes.pacientes import *



class Receptores(Pacientes):
    """
    Esta clase contiene la informacion sobre los pacientes receptores
    """

    def __init__(self, DNI, nombre, fecha_nacimiento, sexo, telefono, sangre, centro_salud_asociado, fecha_lista_espera: datetime, prioridad: int, patologia: str, estado: bool, organo: str):
        super().__init__(DNI, nombre, fecha_nacimiento, sexo, telefono, sangre, centro_salud_asociado)
        self.fecha_lista_espera = fecha_lista_espera
        self.prioridad = prioridad
        self.estado = estado
        self.organo = organo

