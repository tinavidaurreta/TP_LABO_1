from tpfinal.cirujanos.especialista import Especialista
from tpfinal.cirujanos.generales import Generales
from tpfinal.vehiculos.auto import Auto
from tpfinal.vehiculos.helicoptero import Helicoptero
from tpfinal.vehiculos.avion import Avion
from excepciones.excepcion_tiempo import ErrorDeTransplante
from excepciones.expecion_cirujano import ErrDeCirujano
from datetime import datetime, timedelta



class CentrosSalud:
    """
    Esta clase contiene la informacion de los vehiculos y cirujanos  
    """
    
    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str, telefono: int, lista_cirujanos:list[Generales | Especialista], lista_vehiculos: list[ Helicoptero | Auto| Avion]):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia 
        self.telefono = telefono
        self.lista_cirujanos = lista_cirujanos
        self.lista_vehiculos = lista_vehiculos
        pass

    def __str__(self):
        return f"{self.nombre}" 

    def asignar_vehiculo(self, centro_receptor) -> Helicoptero | Auto| Avion:
        """
        Asigna un vehiculo para el transporte del organo
        parametros:
            - centro_receptor: el centro de salud del paciene receptor del transplante 
        returns:
            Retorna un tipo de vehuiculo con una distancia y un registro de viajes
        """
        n = len(self.lista_vehiculos)
        for k in range (0, len(self.lista_vehiculos), 1):
            for i in range(0,len(self.lista_vehiculos)-1, 1): #se ordena la lista de vehiculos segun la mayor velocidad
                if self.lista_vehiculos[i].velocidad < self.lista_vehiculos[i+1].velocidad:
                    transporte = self.lista_vehiculos[i]
                    self.lista_vehiculos[i] = self.lista_vehiculos[i+1]
                    self.lista_vehiculos[i+1] = transporte
        for i in range (0, len(self.lista_vehiculos), 1):
            if self.provincia == centro_receptor.provincia:
                if self.partido == centro_receptor.partido:
                    if type(self.lista_vehiculos[i]) == Auto:
                        vehiculo = self.lista_vehiculos[i]
                        self.lista_vehiculos[i].registro_viaje +=1
                        break
                else:
                    if type(self.lista_vehiculos[i]) == Helicoptero:
                        vehiculo = self.lista_vehiculos[i]
                        self.lista_vehiculos[i].registro_viaje +=1
                        break
            else:
                    if type(self.lista_vehiculos[i]) == Avion:
                        vehiculo = self.lista_vehiculos[i]
                        self.lista_vehiculos[i].registro_viaje +=1
                        break
        return vehiculo
    
    def asignar_cirujano(self)-> Generales | Especialista:
        """
        Asigna un cirujano para el transplante del organo segun su disponibilidad
        returns:
            Devuelve un cirujano para el transplante sea general o especialista
        """
        n = len(self.lista_cirujanos)
        cirujano = 0
        for i in range (0,len(self.lista_cirujanos), 1):
            self.lista_cirujanos[i].ocupacion()
            if not self.lista_cirujanos[i].ocupado:
                cirujano = self.lista_cirujanos[i]
                return cirujano
            elif i == len(self.lista_cirujanos)-1:
                raise ErrDeCirujano()
    
    def realizar_transplante(self, fecha_hora_ablacion: datetime, vehiculo:Helicoptero | Auto| Avion , cirujano: Generales | Especialista, organo_operar: str)-> bool:
        """
        Chequea si transcurrieron mas de 20hrs desde la fecha de ablacion del organo a la fecha del transplante, y sino, define el exito segun el cirujano
        parametros:
            - Fecha_hora_ablacion: fecha de cuando se retiro el organo 
            - vehiculo: vehiculo del transplante, que tiene la informacion de la distancia y el trafico, en horas
            - cirujano: cirujano del transplante
            - organo_operar: organo que se transplanta
        returns:
            Devuelve un bool que si es True significa que el transplante fue exitoso y sino no 
        """
        trayecto = vehiculo.tiempo_trayecto()
        fecha_transplante = datetime.now() + timedelta(hours=trayecto)
        if (fecha_transplante - fecha_hora_ablacion).total_seconds() <= 20* 3600: #compara en segundos
            exito = cirujano.exito(organo_operar) 
            return exito
        else:
            raise ErrorDeTransplante((fecha_transplante - fecha_hora_ablacion).total_seconds())
            
   