from cirujanos import Cirujanos
import random


class Generales(Cirujanos):

    def __init__(self):
        super().__init__()
        self.tipo = "general"

    def exito(self, organo_operar)-> bool: 
        """
        Informo el exito de la operacion segun un numero aleatorio
        """
        numero = random.randint(1,10)
        return (numero>5)
