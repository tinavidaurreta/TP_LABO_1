from vehiculos.vehiculos import *



class Auto(Vehiculos):
    """ 
    Esta clase contiene la informacion de un auto
    """

    def __init__(self, velocidad, registro_viaje, dist, trafico):
        super().__init__(velocidad, registro_viaje, dist, trafico)

    def __str__(self):
        return "Auto"
    
    def tiempo_trayecto(self) -> int:
        """ 
        Calculo el tiempo de trayecto a partir de la velocidad, la distancia y el trafico
        returns:
            Retorna en horas el tiempo total del trayecto incluyendo al trafico
        """ 
        return  (self.dist + self.trafico) / self.velocidad 


 