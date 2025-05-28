from tpfinal.pacientes.receptores import *
from tpfinal.pacientes.donantes import *
from centros_salud import *



class Incucai: 
    """
        Esta clase se encarga de unir la lista de centros de salud con los pacientes y donantes, realizando los transplantes y registrando a los pacientes correcpondientes
    """

    def __init__(self, lista_receptores: list[Receptores], lista_donantes: list[Donantes], lista_centros_salud: list[CentrosSalud]):
        self.lista_receptores = lista_receptores
        self.lista_donantes = lista_donantes
        self.lista_centros_salud = lista_centros_salud

    def prioridad_receptores(self)-> None:
        """
        Ordena la lista de pacientes receptors de mayor a menor prioridad (1: menor 5: mayor)
        """
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
        return
    
    def trasladar_organo(self, pos_receptor: int, pos_donante: int)-> None: 
        """ 
        Realiza el transplante con vehiculo y cirujano asignado y verifica su exito, eliminando al paciente receptor y el organo utilizado del donante
        parametros:
            - pos_receptor: la posicion del receptor del transplante en la lista de receptores
            - pos_donante: la posicion del donante del transplante en la lista de donantes
        precon:
            - se debe cumplir que se encuentre un cirujano disponible
            - se debe cumplir que el tiempo del trayecto no supere las 20 horas
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
                    print(f"El transplante no fue exitoso, el paciente {self.lista_receptores[pos_receptor]} se encuentra inestable y pasa a ser el paciente con mayor prioridad")
            finally:
                return
        finally:
            return

    def registrar_paciente_donante(self, paciente_donante: Donantes)-> None: 
        """ 
        Chequea que el paciente ingresado no este anteriormente registrado
        parametros:
            - paciente_donante: donante que se va a registrar
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
        for i in range(0,len (self.lista_receptores)-1,1): # recorre la lista de receptores 
            if self.lista_donantes[n-1].sangre == self.lista_receptores[i].sangre:
                for j in range(0,len(self.lista_donantes[n-1].listado_organos_donar),1):
                    if self.lista_donantes[n-1].listado_organos_donar[j] == self.lista_receptores[i].organo:
                        pos_receptor = i
                        pos_organo = j
                        self.trasladar_organo(pos_receptor,n-1) #ya que la lista esta ordenada de mayor prioridad a menor
                        """ 
                        Se elimina de la lista de organos del donante el organo que recibira el receptor ya encontrado o, si es su ultimo organo, se elimina al donante de la lista
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

    def registrar_paciente_receptor(self, paciente_receptor: Receptores)-> None:
        """
        Chequea que el paciente ingresado no este anteriormente registrado
        parametros:
            - paciente_receptor: receptor que se va a registrar
        """
        for receptor in self.lista_receptores:
            if paciente_receptor.dni == receptor.dni:
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
                    
    def imprimir_donantes_receptores(self)-> None:
        """
        Imprime el listado de pacientes donantes y receptores
        """
        n = len (self.lista_donantes)
        c = len (self.lista_receptores)
        print("Pacientes\nDonantes                Receptores")
        for i in range(max(n,c)):
            if i<n: 
                donante = self.lista_donantes[i]
            else: 
                donante = "-"
            if i<c: 
                receptor = self.lista_receptores[i]
            else: 
                receptor = "-"

            print(f"{i+1}. {str(donante):<20}  {str(receptor)}")
        return 
    
    def prioridad_paciente(self, dni: int)-> int:
        """
        Busca e imprime la prioridad del paciente receptor ingresado y retorna un numero, 0 si pertenece a un donante, 1, si es de un receptor o -1 si no se encuentra registrado
        parametros:
            - dni: dni de paciente a buscar
        return
            Un numero, 0 si el dni es de un donante, -1 si se busca un paciente no registrado o 1 si se imprime la prioridad buscada
        """
        n = len(self.lista_receptores)
        c = len(self.lista_donantes)
        for i in range(c):
            if dni == self.lista_donantes[i].dni:
                print("El DNI ingresado pertenece a un paciente donante")
                return 0
        for i in range(n):
            if dni == self.lista_receptores[i].dni:
                print (f"La prioridad del paciente ingresado es {self.lista_receptores[i].prioridad}")
                return 1
        print ("El DNI ingresado no pertenece a un paciente registrado")
        return -1
    
    def imprimir_lista_espera(self, centro_salud: CentrosSalud)-> None:
        """
        Imprime la lista de espera segun el centro de salud
        """
        c = len (self.lista_receptores)
        print(f"Pacientes de {centro_salud}\nReceptores")
        for i in range(c):
            if self.lista_receptores[i].centro_salud == centro_salud: 
                receptor = self.lista_receptores[i]
            else: 
                receptor = "-"
            print(f"{i+1}.{str(receptor)}")
        return 



