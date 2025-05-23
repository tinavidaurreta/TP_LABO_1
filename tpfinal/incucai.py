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
        for i in range (1,len(self.lista_receptores)-1,1):
            for j in range (0,m-i,1): # el ordenamiento es de abajo hacia arriba, quedando en la primer posicion a quien reciba el trasplante
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
        organo_operar = self.lista_receptores[pos_receptor].organo
        vehiculo = centro_donante.asignar_vehiculo(centro_receptor) # el centro de salud del donante asigna un vehiculo
        try:
            cirujano = centro_donante.asignar_cirujano() # el centro de salud del donante asigna un cirujano
        except ErrDeCirujano as e:
            print(e)
        else:
            cirujano = centro_donante.asignar_cirujano() # el centro de salud del donante asigna un cirujano
            self.lista_donantes[pos_donante].seteo_fecha() # se setea la fecha de ablacion del organo donante
            n = len(self.lista_receptores)
            print(f"El cirujano asignado para el transplante es {cirujano}")
            print(f"La velocidad del vehiculo asignado {vehiculo} para el transplante es {vehiculo.velocidad}")
            try:
                exito = centro_receptor.realizar_transplante(self.lista_donantes[pos_donante].fecha_hora_ablacion,vehiculo,cirujano,organo_operar)
            except ErrorDeTransplante as e:
                print(e)
            else: 
                """ 
                Chequea si el transplante fue exitoso (elimina al receptor de la lista) o no
                """
                if exito :
                    if pos_receptor < len(self.lista_receptores) - 1:
                        for i in range(pos_receptor,len(self.lista_receptores)-1,1):
                            self.lista_receptores[i] = self.lista_receptores[i+1]
                    self.lista_receptores = self.lista_receptores[:-1]
                    print("El transplante fue exitoso")
                else:
                    self.lista_receptores[pos_receptor].prioridad = 1
                    self.lista_receptores[pos_receptor].estado = False # Inestable: False, Estable: True
                    print("El transplante no fue exitoso, el paciente se encuentra inestable y pasa a ser el paciente con mayor prioridad")
            finally:
                return
        finally:
            return

    def registrar_paciente_donante(self, paciente_donante: Donantes): 
        """ 
        Chequea que el paciente ingresado no este anteriormente registrado
        """
        for donante in self.lista_donantes:
            if paciente_donante == donante:
                print("El paciente ya fue registrado")
                return  # sale de la función si ya estaba
        self.lista_donantes.append(paciente_donante)
        print("Se ha registrado al donante correctamente") 
        """
        Se busca al receptor correspondiente segun su tipo de sangre y organo y se lo guarda en la lista de compatibles.
        """
        n = len(self.lista_donantes)
        self.prioridad_receptores()
        k = len(self.lista_donantes[n-1].listado_organos_donar)
        for i in range(0,len (self.lista_receptores),1): # recorre la lista de receptores 
            if self.lista_donantes[n-1].sangre == self.lista_receptores[i].sangre:
                for j in range(0,len(self.lista_donantes[n-1].listado_organos_donar),1):
                    if self.lista_donantes[n-1].listado_organos_donar[j] == self.lista_receptores[i].organo:
                        pos_receptor = i
                        pos_organo = j
                        self.trasladar_organo(pos_receptor,n-1) #ya que la lista esta ordenada de mayor prioridad a menor
                        """ 
                        Se elimina de la lista de organos del donante el organo que recibira el receptor ya encontrado o si es su ultimo organo se elimina al donante de la lista
                        """
                        if k == 1:
                            for r in range(n-1,len(self.lista_donantes)-1,1): # borra al donante ya que solo donaba uno solo
                                self.lista_donantes[r] = self.lista_donantes[r+1]
                                self.lista_donantes = self.lista_donantes[:-1]
                        else:
                            for l in range(pos_organo,len(self.lista_donantes[n-1].listado_organos_donar)-1,1): # borra el organo del donante
                                self.lista_donantes[n-1].listado_organos_donar[l] = self.lista_donantes[n-1].listado_organos_donar[l+1]
                            self.lista_donantes[n-1].listado_organos_donar = self.lista_donantes[n-1].listado_organos_donar[:-1]
                        break
        return

    def registrar_paciente_receptor(self, paciente_receptor: Receptores):
        """
        Chequea que el paciente ingresado no este anteriormente registrado
        """
        for receptor in self.lista_receptores:
            if paciente_receptor == receptor:
                print("El paciente ya fue registrado")
                return  # sale de la función si ya estaba
        self.lista_receptores.append(paciente_receptor)
        print("Se ha registrado al receptor correctamente") 
        """
        Se busca al organo del donante correspondiente segun su tipo de sangre y organo.
        """
        n = len(self.lista_receptores)
        c = len (self.lista_donantes)
        for i in range(0,len(self.lista_donantes)): # recorre la lista donantes.
            if self.lista_receptores[n-1].sangre == self.lista_donantes[i].sangre:
                k = len(self.lista_donantes[i].listado_organos_donar)
                for j in range(0,len(self.lista_donantes[i].listado_organos_donar),1): #recorre la lista de organos de ese donante
                    if self.lista_receptores[n-1].organo == self.lista_donantes[i].listado_organos_donar[j]:
                        pos_donante = i
                        pos_organo = j
                        self.trasladar_organo (n-1, pos_donante)
                        if k == 1:
                            for r in range(pos_donante,len (self.lista_donantes)-1,1): # borra al donante ya que solo donaba uno solo
                                self.lista_donantes[r] = self.lista_donantes[r+1]
                                self.lista_donantes = self.lista_donantes[:-1]
                        else:
                            for l in range(pos_organo,len(self.lista_donantes[pos_donante].listado_organos_donar)-1,1): # borra el organo del donante
                                self.lista_donantes[pos_donante].listado_organos_donar[l] = self.lista_donantes[pos_donante].listado_organos_donar[l+1]
                            self.lista_donantes[pos_donante].listado_organos_donar = self.lista_donantes[pos_donante].listado_organos_donar[:-1]
                        break
        return           
                    

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
    




