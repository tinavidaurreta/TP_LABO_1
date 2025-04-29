from pacientes import *



class Donantes(Pacientes):

    def __init__(self, DNI, nombre, fecha_nacimiento, sexo, telefono, sangre, centro_salud_asociado, fecha_fallecimiento_hora: datetime, fecha_hora_ablacion: datetime, listado_organos_donar: list[Organos]):
        super().__init__(DNI, nombre, fecha_nacimiento, sexo, telefono, sangre, centro_salud_asociado)
        self.fecha_hora_fallecimiento = fecha_fallecimiento_hora
        self.fecha_hora_ablacion = fecha_hora_ablacion
        self.listado_organos_donar = listado_organos_donar