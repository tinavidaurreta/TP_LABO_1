from abc import ABC, abstractmethod
import random

class Cirujanos(ABC): 

    def __init__(self,nombre: str):
        self.ocupado = False
        self.nombre = nombre

    def __str__(self):
        return f"Nombre: {self.nombre}" 
        
    @abstractmethod

    def exito(self, organo_operar: str)->int:
        """
        Define el exito de la operacion
        """
        numero = random.randint(1,10)
        return (numero>5)

