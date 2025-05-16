from receptores import *
from donantes import *
from centros_salud import *



class Incucai: 

    def __init__(self, lista_receptores: list[Receptores], lista_donantes: list[Donantes], lista_centros_salud: list[CentrosSalud]):
        self.lista_receptores = lista_receptores
        self.lista_donantes = lista_donantes
        self.lista_centros_salud = lista_centros_salud

    def prioridad_receptores(self):
        m = len(self.lista_receptores)
        for i in range (1,m-1,1):
            for j in range (0,m-i-1,1): # el ordenamiento es de abajo hacia arriba, quedando en la primer posicion a quien reciba el trasplante
                if self.lista_receptores[j].prioridad > self.lista_receptores[j+1].prioridad:
                    receptor = self.lista_receptores[j]
                    self.lista_receptores[j] = self.lista_receptores[j+1]
                    self.lista_receptores[j+1] = receptor
                elif self.lista_receptores[j].prioridad == self.lista_receptores[j+1].prioridad:
                    if  self.lista_receptores[j].fecha_lista_espera < self.lista_receptores[j+1].fecha_lista_espera:
                        receptor = self.lista_receptores[j]
                        self.lista_receptores[j] = self.lista_receptores[j+1]
                        self.lista_receptores[j+1] = receptor
    
    def trasladar_organo(self, pos_receptor: int, pos_donante: int): 
        """ 
        Realiza el transplante con vehiculo y cirujano asignado
        """
        centro_donante = self.lista_donantes[pos_donante].centro_salud
        centro_receptor = self.lista_receptores[pos_receptor].centro_salud
        vehiculo = centro_donante.asignar_vehiculo(centro_receptor) # el centro de salud del donante asigna un vehiculo
        cirujano = centro_donante.asignar_cirujano() # el centro de salud del donante asigna un cirujano
        self.lista_donantes[pos_donante].seteo_fecha() # se setea la fecha de ablacion del organo donante
        numero_exito = centro_receptor.realizar_transplante(self.lista_donantes[pos_donante].fecha_hora_ablacion,vehiculo,cirujano)
        n = len(self.lista_receptores)
        """ 
        Chequea si el transplante fue exitoso (elimina al receptor de la lista) o no
        """
        if (numero_exito >= 3 and cirujano == type(Especialista)) or (numero_exito>=5 and cirujano == type(Generales)) :
            for i in range(pos_receptor,n-1,1):
                self.lista_receptores[i] = self.lista_receptores[i+1]
            print("El transplante fue exitoso")
        else:
            self.lista_receptores[pos_receptor].prioridad = 1
            self.lista_receptores[pos_receptor].estado = False # Inestable: False, Estable: True
            print("El transplante no fue exitoso, el paciente se encuentra inestable y pasa a ser el paciente con mayor prioridad")
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
        self.prioridad_receptores()
        k = len(self.lista_donantes[n].listado_organos_donar)
        c = len (self.lista_receptores)
        for i in range(0,c,1): # recorre la lista de receptores y una posicion mas para luego ver si no encontro match
            if self.lista_donantes[n].sangre == self.lista_receptores[i].sangre:
                for j in range(0,k-1,1):
                    if self.lista_donantes[n].listado_organos_donar[j] == self.lista_receptores[i].organo:
                        pos_receptor = i
                        break #ya que la lista esta ordenada de mayor prioridad a menor
        if i == c : # si es c es porque llego hasta una posicion de mas en el ciclo for
            self.trasladar_organo(self,pos_receptor,n)
            """ 
            Se elimina de la lista de organos del donante el organo que recibira el receptor ya encontrado o si es su ultimo organo se elimina al donante de la lista
            """
            for i in range(0,k-1,1):
                if self.lista_donantes[n].listado_organos_donar[i] == self.lista_receptores[pos_receptor].organo:
                        if i == 0: # elimino al donante de la lista de donantes
                                self.lista_donantes[n] = None
                                self.lista_donantes = self.lista_donantes[:-1]
                        else:
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
                        if k == 1:
                            for r in range(pos_donante,c-1,1): # borra al donante ya que solo donaba uno solo
                                self.lista_donantes[r] = self.lista_donantes[r+1]
                        else:
                            for l in range(i,k-1,1): # borra el organo del donante
                                self.lista_donantes[n].listado_organos_donar[l] = self.lista_donantes[n].listado_organos_donar[l+1]
        return print("Se ha registrado al receptor correctamente")               

    def imprimir_donantes_receptores(self):
        """
        Imprime el listado de pacientes donantes y receptores
        """
        n = len (self.lista_donantes)
        c = len (self.lista_receptores)
        print("Pacientes\nDonantes     Receptores")
        for i in range(0, max(n,c), 1):
            print(f"{i}. {self.lista_donantes[i]}  {self.lista_receptores[i]}"  )
        return 
    


            




