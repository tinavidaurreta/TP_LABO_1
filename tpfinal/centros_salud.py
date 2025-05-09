from especialista import Especialista
from generales import Generales
from auto import Auto
from helicoptero import Helicoptero
from avion import Avion
import datetime


class CentrosSalud:

    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str, telefono: int, lista_cirujanos:list[Generales | Especialista], lista_vehiculos: list[ Helicoptero | Auto| Avion]):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia 
        self.telefono = telefono
        self.lista_cirujanos = lista_cirujanos
        self.lista_vehiculos = lista_vehiculos
        pass

    def asignar_vehiculo(self, centro_receptor) -> Helicoptero | Auto| Avion:
        """
            Asigna un vehiculo para el transporte del organo, segun el centro del donante '1' y el rececptor '2'
        """
        n = len(self.lista_vehiculos)
        for k in range (0, n-1, 1):
            for i in range(0, n-1, 1): #se ordena la lista de vehiculos segun la mayor velocidad
                if self.lista_vehiculos[i].velocidad < self.lista_vehiculos[i+1].velocidad:
                    transporte = self.lista_vehiculos[i]
                    self.lista_vehiculos[i] = self.lista_vehiculos[i+1]
                    self.lista_vehiculos[i] = transporte
        for i in range (0, n-1, 1):
            if self.provincia == centro_receptor.provincia:
                if self.partido == centro_receptor.partido:
                    if self.lista_vehiculos[i] == type(Auto):
                        vehiculo = self.lista_vehiculos[i]
                        break
                else:
                    if self.lista_vehiculos[i] == type(Helicoptero):
                        vehiculo = self.lista_vehiculos[i]
                        break
            else:
                    if self.lista_vehiculos[i] == type(Avion):
                        vehiculo = self.lista_vehiculos[i]
                        break
        return vehiculo
    
    def asignar_cirujano(self)-> Generales | Especialista:
        """
        Asigna un cirujano para el transplante del organo segun su disponibilidad
        """
        n = len(self.lista_cirujanos)
        for i in range (0,n-1, 1):
            if ~self.lista_cirujanos[i].ocupado:
                cirujano = self.lista_cirujanos[i]
                self.lista_cirujanos[i].ocupado == True
            else:
                print("Ningun cirujano se encuentra disponible")
        
        return cirujano
    
    def realizar_transplante(self, fecha_hora_ablacion: datetime, vehiculo:Helicoptero | Auto| Avion , cirujano: Generales | Especialista)-> int:
        """
        Define si transcurrieron mas de 20hrs desde la fecha de ablacion del organo a la fecha del transplante
        """
        trayecto = vehiculo.tiempo_trayecto()
        fecha_transplante = datetime.now() + trayecto
        if fecha_transplante - fecha_hora_ablacion <= 20:
            exito = cirujano.exito()
        else:
            print("Transcurrieron mas de 20hrs de la fecha de ablacion")
        return exito
    