from tpfinal.vehiculos.vehiculos import *



class Auto(Vehiculos):
    """ 
    Esta clase contiene la informacion de un auto
    """

    def __init__(self, velocidad, registro_viaje, dist, trafico):
        super().__init__(velocidad, registro_viaje, dist, trafico)

    def tiempo_trayecto(self) -> int:
        """ 
        Calculo el tiempo de trayecto a partir de la velocidad, la distancia y el trafico
        """ 
        return  (self.dist + self.trafico) / self.velocidad 


 