from abc import ABC, abstractmethod


class Cirujanos(ABC): 

    def __init__(self):
        self.ocupado = False
        pass


@abstractmethod

def exito(self, organo_operar: str)->int:
    """
    Define el exito de la operacion
    """

