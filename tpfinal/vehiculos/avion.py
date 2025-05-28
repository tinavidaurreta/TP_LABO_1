from tpfinal.vehiculos.vehiculos import *



class Avion(Vehiculos):
    """ 
    Esta clase contiene la informacion de un avion
    """

    def __init__(self, velocidad, registro_viaje, dist, trafico):
        super().__init__(velocidad, registro_viaje, dist, trafico)

    def tiempo_trayecto(self) -> int:
        """ 
        Calculo el tiempo de trayecto a partir de la velocidad y la distancia
        returns:
            Retorna en horas el tiempo total del trayecto 
        """
        return (self.dist)/ self.velocidad


 