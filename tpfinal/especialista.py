from cirujanos import Cirujanos
import random


class Especialista(Cirujanos):

    def __init__(self,tipo: str):
        super().__init__()

    def exito(self)-> bool: 
        """
        Informo el exito de la operacion segun el organo a operar
        """
        numero = random.randint(1,10)
        if (self.tipo == "cardiovascular" and self.organo_operar == "corazon" ) or (self.tipo == "pulmonar" and self.organo_operar == "pulmones") or (self.tipo == "plastico" and (self.organo_operar == "piel" or self.organo_operar == "corneas")) or (self.tipo == "traumatologo" and self.organo_operar == "huesos") or (self.tipo == "gastroenterologo" and (self.organo_operar == "intestinos" or self.organo_operar == "higado" or self.organo_operar == "riñon" or self.organo_operar == "pancreas")):
            return (numero>=3)
        else:
            return (numero>5)
