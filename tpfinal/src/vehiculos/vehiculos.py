from abc import ABC, abstractmethod



class Vehiculos(ABC):
    """ 
    Esta clase (padre) contiene la informacion de cada vehiculo
    """
    
    def __init__(self, velocidad: int, registro_viaje: int, dist: int, trafico: int):
        self.velocidad = velocidad
        self.registro_viaje = registro_viaje
        self.dist = dist
        self.trafico = trafico
    
    @abstractmethod
    def tiempo_trayecto(self) -> int:
        """ 
        Calculo el tiempo de trayecto a partir de la velocidad, la distancia y el trafico
        returns:
            Retorna en horas el tiempo total del trayecto 
        """
        pass
    
    
