from cirujanos import Cirujanos
import random


class Especialista(Cirujanos):

    def __init__(self, tipo: str):
        super().__init__()
        self.tipo = tipo

    def exito(self, organo_operar)-> bool: 
        """
        Informo el exito de la operacion segun el organo a operar
        """
        numero = random.randint(1,10)
        if (self.tipo == "cardiovascular" and organo_operar == "corazon" ) or (self.tipo == "pulmonar" and organo_operar == "pulmones") or (self.tipo == "plastico" and (organo_operar == "piel" or organo_operar == "corneas")) or (self.tipo == "traumatologo" and organo_operar == "huesos") or (self.tipo == "gastroenterologo" and (organo_operar == "intestinos" or organo_operar == "higado" or organo_operar == "riñon" or organo_operar == "pancreas")):
            return (numero>=3)
        else:
            return (numero>5)
