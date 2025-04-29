from receptores import *
from donantes import *
from centros_salud import *



class Incucai: 

    def __init__(self, lista_receptores: list[Receptores], lista_donantes: list[Donantes], lista_centros_salud: list[centrosSalud]):
        self.lista_receptores = lista_receptores
        self.lista_donantes = lista_donantes
        self.lista_centros_salud = lista_centros_salud
        
    def registrar_paciente_donante(self, paciente_donante: Donantes):
        n = len(self.lista_donantes)
        for i in self.lista_donantes:
           if paciente_donante == self.lista_donantes[i]:
               print ("El paciente ya fue registrado")
               break
           else:
               self.lista_donantes[n+1] = paciente_donante
               break
           
    def registrar_paciente_receptor(self, paciente_receptor: Receptores):
        n = len(self.lista_receptores)
        for i in self.lista_receptores:
           if paciente_receptor == self.lista_receptores[i]:
               break
           else:
               self.lista_receptores[n+1] = paciente_receptor
               break
               




