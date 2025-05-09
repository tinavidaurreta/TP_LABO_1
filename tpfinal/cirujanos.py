from abc import ABC, abstractmethod
from receptores import *


class Cirujanos(ABC): 

    def __init__(self, paciente: Receptores ):
        self.ocupado = False
        self.organo_operar = paciente.organo
        pass


@abstractmethod

def exito(self)->int:
    """
    Define el exito de la operacion
    """

