from receptores import *
from donantes import *
from centros_salud import *



class Incucai: 

    def __init__(self, lista_receptores: list[Receptores], lista_donantes: list[Donantes], lista_centros_salud: list[CentrosSalud]):
        self.lista_receptores = lista_receptores
        self.lista_donantes = lista_donantes
        self.lista_centros_salud = lista_centros_salud
    
    def trasladar_organo(self, pos_receptor: int, pos_donante: int):  
        
        return

    def registrar_paciente_donante(self, paciente_donante: Donantes): 
        """ 
        Chequea que el paciente ingresado no este anteriormente registrado
        """
        n = len(self.lista_donantes)
        for i in range(0,n-1,1):
           if paciente_donante == self.lista_donantes[i]:
               print ("El paciente ya fue registrado")
               break
           else:
               self.lista_donantes[n] = paciente_donante
               break
        """
        Se busca al receptor correspondiente segun su tipo de sangre y organo y se lo guarda en la lista de compatibles.
        """
        compatibles = list[Receptores]
        m = 0
        k = len(self.lista_donantes[n].listado_organos_donar)
        c = len (self.lista_receptores)
        for i in range(0,c-1,1): # recorre la lista de receptores.
            if self.lista_donantes[n].sangre == self.lista_receptores[i].sangre:
                for j in range(0,k-1,1):
                    if self.lista_donantes[n].listado_organos_donar[j] == self.lista_receptores[i].organo:
                        compatibles[m]= self.lista_receptores[i]
                        m=+1
        """ 
       Se busca al receptor con mayor prioridad (1: mas, 5:menos) o, en caso de tener una misma, el que mayor antelacion tenga en la lista
        """
        m = len(compatibles)
        for i in range (1,m-1,1):
            for j in range (0,m-i-1,1): # el ordenamiento es de abajo hacia arriba, quedando en la primer posicion a quien reciba el trasplante
                if compatibles[j].prioridad > compatibles[j+1].prioridad:
                    receptor = compatibles[j]
                    compatibles[j] = compatibles[j+1]
                    compatibles[j+1] = receptor
                elif compatibles[j].prioridad == compatibles[j+1].prioridad:
                    if  compatibles[j].fecha_lista_espera < compatibles[j+1].fecha_lista_espera:
                        receptor = compatibles[j]
                        compatibles[j] = compatibles[j+1]
                        compatibles[j+1] = receptor
        """ 
        Se busca la posicion del receptor en la lista de receptores del Incucai
        """
        for i in range (0,c-1,1):
            if compatibles[0] == self.lista_receptores[i]:
                pos_receptor = i
        if m != 0 : # si es 0 es porque no hubo coincidencia con ningun receptor
            self.trasladar_organo(self,pos_receptor,n)
            """ 
            Se elimina de la lista de organos del donante el organo que recibira el receptor ya encontrado
            """
            for i in range(0,k,1):
                if self.lista_donantes[n].listado_organos_donar[i] == compatibles[0].organo:
                        for j in range(i,k,1):
                            self.lista_donantes[n].listado_organos_donar[j] = self.lista_donantes[n].listado_organos_donar[j+1]
        return print("Se ha registrado el donante correctamente")

    def registrar_paciente_receptor(self, paciente_receptor: Receptores):
        n = len(self.lista_receptores)
        """
        Chequea que el paciente ingresado no este anteriormente registrado
        """
        for i in range(0,n-1,1):
           if paciente_receptor == self.lista_receptores[i]:
               break
           else:
               self.lista_receptores[n] = paciente_receptor
               break
        """
        Se busca al organo del donante correspondiente segun su tipo de sangre y organo y se lo guarda en la lista de compatibles.
        """
        c = len (self.lista_donantes)
        for i in range(0,c-1,1): # recorre la lista donantes.
            if self.lista_receptores[n].sangre == self.lista_donantes[i].sangre:
                k = len(self.lista_donantes[i].listado_organos_donar)
                for j in range(0,k-1,1): #recorre la lista de organos de ese donante
                    if self.lista_receptores[n].organo == self.lista_donantes[i].listado_organos_donar[j]:
                        pos_donante = i
                        self.trasladar_organo (self, n, pos_donante)
                        for l in range(i,k,1): # borra el organo del donante
                            self.lista_donantes[n].listado_organos_donar[l] = self.lista_donantes[n].listado_organos_donar[l+1]
                            break
        return print("Se ha registrado al receptor correctamente")               


            




