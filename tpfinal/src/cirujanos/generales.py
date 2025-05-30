from cirujanos.cirujanos import Cirujanos
import random


class Generales(Cirujanos):
    """
    Esta clase contiene la informacion de cada cirujano general
    """

    def __init__(self, nombre):
        super().__init__(nombre)
        self.tipo = "general"

    def exito(self, organo_operar: str)-> bool: 
        """
        Informo el exito de la operacion segun un numero aleatorio
        parametros:
            - organo_operar: el organo del transplante
        returns:
            Retorna un True si el numero random es mayor a 5
        """
        numero = random.randint(1,10)
        return (numero>5)
