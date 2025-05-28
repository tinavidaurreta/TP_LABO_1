from abc import ABC, abstractmethod
import random
from datetime import date

class Cirujanos(ABC):
    """
    Esta clase (padre) contiene la informacion de cada cirujano
    """

    def __init__(self,nombre: str):
        self.ocupado = False
        self.dia_trabajo = 0
        self.nombre = nombre

    def __str__(self):
        return f"Nombre: {self.nombre}" 
    
    def ocupacion(self)-> None:
        """
        Chequea si el cirujano ya opero ese dia
        """
        if self.dia_trabajo == date.today():
           self.ocupado = True
        elif self.dia_trabajo == 0:
            self.ocupado = False
            self.dia_trabajo = date.today()
        else:
            self.ocupado = False
            return
        
    @abstractmethod

    def exito(self, organo_operar: str)->bool:
        """
        Define el exito de la operacion
        parametros:
            - organo_operar: el organo del transplante
        returns:
            Retorna un True si el numero random es mayor a 5
        """
        numero = random.randint(1,10)
        return (numero>5)

