from incucai import *
import random 

DRFELIPE = Generales('Dr.Felipe')
DRAMARTINA = Especialista('Dra.Martina','cardiovascular')
DRALFREDO = Especialista('Dr.Alfredo','pulmonar')
DRSEBASTIAN = Especialista('Dr.Sebastian','traumatologo')
DRJOAQUIN = Generales('Dr.Joaquin')
DRAMERCEDES = Especialista('Dra.Mercedes','plastico')
DRJAVIER = Especialista('Dr.Javier','gastroenterologo')
HELICOPTERO = Helicoptero(300, 0, 500, 0)#TRAFICO SE SUMA EN KM A LA DIST
AVION = Avion(800, 0, 1000, 0)
AUTO_1 = Auto(100, 0, 50, 0)
AUTO_2 = Auto(60, 0, 80, 0)
AUTO_3 = Auto(130, 0, 150, 0)
ALEMAN = CentrosSalud('Aleman', 'Av.Pueyrredon 1640', 'CABA', 'BuenosAires', 1148277000, [DRFELIPE],[HELICOPTERO,AVION,AUTO_1, AUTO_2, AUTO_3])
SWISSMEDICAL = CentrosSalud('SwissMedical', 'SanMartindeTours 2980', 'Capital', 'Cordoba', 8103338876 , [DRALFREDO], [HELICOPTERO,AVION,AUTO_3])
BRITANICO = CentrosSalud('Britanico', 'Solis 2171','CABA','BuenosAires', 1143096400, [DRJAVIER],[AUTO_1,AUTO_2,AUTO_3, AVION,HELICOPTERO])
AUSTRAL = CentrosSalud('Austral', 'Av.Pres.JuanDomingoPeron 1500', 'Pilar', 'BuenosAires', 2304482000 , [DRAMERCEDES,DRJOAQUIN], [HELICOPTERO,AVION,AUTO_2])
fecha_clara = datetime(2004, 5, 14)
fecha_simon = datetime(2004, 2, 13)
fecha_felipe = datetime(2004, 12, 18)
fecha_justo = datetime(2003, 5, 20)
CLARA = Donantes(46111111, 'Clara Gomez', fecha_clara, 'F', 1128112222, 'AB', ALEMAN, 0, 0, ['corazon', 'piel', 'higado','pancreas'])
SIMON = Receptores(46222222, 'Simon Villanueva',fecha_simon, 'M', 1123459876, 'A', SWISSMEDICAL, 0 , 4, 'hepatitis', False, 'higado')# Inestable: False, Estable: True
FELIPE = Receptores(46333333, 'Felipe Nini',fecha_felipe, 'M', 1145454545, 'A' , AUSTRAL, 0, 2, 'FibrosisQuistica', True, 'pulmon')
JUSTO = Receptores(46444444, 'Justo Larguia', fecha_justo, 'M', 1145451111, 'B', ALEMAN, 0, 3, 'Paro', True, 'corazon')
receptores=[FELIPE, SIMON, JUSTO]
donantes = [CLARA]
INCUCAI= Incucai(receptores,donantes,[SWISSMEDICAL,AUSTRAL,ALEMAN,BRITANICO])

def menu(opcion):
    match opcion:
        case 1:
            for i in range(5):
                try:
                    cantidad = int(input('Ingrese cuanta cantidad de pacientes quiere registrar'))
                except ValueError:
                    print('Debe ingresar un número entero para la cantidad.')
                    cantidad = 0
                if cantidad > 0:
                    j = 0
                    while j < cantidad:
                        x = input('Ingrese "R" si va a ingresar un paciente receptor o ingrese "D" si va a ingresar un paciente donante:').upper()
                        if x == 'R' :
                            try:
                                DNI = int(input ('Ingrese su DNI:')) #ELEMENTAL
                            except ValueError:
                                print('Debe ingresar un número entero para el DNI.')
                                DNI = 0
                            nombre_apellido = input ('Ingrese su nombre y apellido:')
                            fecha_str = input('Ingrese una fecha de nacimiento en formato DD/MM/AAAA:')
                            sexo = input ('Ingrese su F o M segun su sexo:').upper()
                            telefono = input ('Ingrese su numero de telefono:')
                            tipo_sangre = -1
                            while tipo_sangre == -1:
                                tipo_sangre = input ('Ingrese su tipo de sangre (A / AB / B / 0):').upper() 
                                if tipo_sangre not in["A" ,"B" ,"AB" , "0"]:
                                    print('Por favor, ingrese un tipo de sangre valido.')
                                    tipo_sangre = -1
                            prioridad = random.randint(1,5)
                            centro_salud = None
                            while centro_salud == None:
                                try:
                                    centro_salud_num = int(input('Ingrese su centro de salud afiliado: (1. ALEMAN 2. SWISSMEDICAL 3. AUSTRAL 4. BRITANICO): '))
                                    if centro_salud_num == 1 :
                                        centro_salud = ALEMAN
                                    elif centro_salud_num == 2:
                                        centro_salud = SWISSMEDICAL
                                    elif centro_salud_num == 3:
                                        centro_salud = AUSTRAL 
                                    elif centro_salud_num == 4:
                                        centro_salud = BRITANICO
                                    else: 
                                        print('Por favor, ingrese un número válido.')
                                        centro_salud = None
                                except ValueError:
                                    print('Por favor, ingrese un número válido.')
                                    centro_salud = None
                            patologia = input ('Ingrese su patologia:')
                            organo = input ('Ingrese el organo necesitante:').lower()
                            fecha_lista_espera = datetime.now()
                            PACIENTE_RECEPTOR = Receptores(DNI, nombre_apellido, fecha_str, sexo, telefono, tipo_sangre, centro_salud, fecha_lista_espera, prioridad, patologia, True, organo) # Siempre True hasta que se opere y cambie
                            INCUCAI.registrar_paciente_receptor(PACIENTE_RECEPTOR)
                            j += 1
                        elif x == 'D':
                            DNI = input ('Ingrese su DNI:')
                            nombre_apellido = input ('Ingrese su nombre y apellido:')
                            fecha_str = input('Ingrese una fecha de nacimiento en formato DD/MM/AAAA: ')
                            sexo = input ('Ingrese su F o M segun su sexo:')
                            telefono = input ('Ingrese su numero de telefono:')
                            tipo_sangre = -1
                            while tipo_sangre == -1:
                                tipo_sangre = input ('Ingrese su tipo de sangre (A / AB / B / 0):').upper() 
                                if tipo_sangre not in["A" ,"B" ,"AB" , "0"]:
                                    print('Por favor, ingrese un tipo de sangre valido.')
                                    tipo_sangre = -1
                            centro_salud = None
                            fecha_fallecimiento_hora = datetime.now()
                            fecha_hora_ablacion = 0
                            while centro_salud == None:
                                try:
                                    centro_salud_num = int(input('Ingrese su centro de salud afiliado: (1. ALEMAN 2. SWISSMEDICAL 3. AUSTRAL 4. BRITANICO): '))
                                    if centro_salud_num == 1 :
                                        centro_salud = ALEMAN
                                    elif centro_salud_num == 2:
                                        centro_salud = SWISSMEDICAL
                                    elif centro_salud_num == 3:
                                        centro_salud = AUSTRAL 
                                    elif centro_salud_num == 4:
                                        centro_salud = BRITANICO
                                    else: 
                                        print('Por favor, ingrese un número válido.')
                                        centro_salud = None
                                except ValueError:
                                    print('Por favor, ingrese un número válido.')
                                    centro_salud = None
                            organos = input ('Ingrese el/los organos donantes:').lower()
                            palabra = ""
                            lista_organos = []
                            for caracter in organos:
                                if caracter != " ":
                                    palabra += caracter  # va construyendo la palabra
                                elif palabra:
                                        lista_organos.append(palabra)
                                        palabra = ""  # reinicia para la siguiente palabra            
                            if palabra:# Añadir la última palabra si no termina con espacio
                                lista_organos.append(palabra)
                            PACIENTE_DONANTE = Donantes(DNI, nombre_apellido, fecha_str, sexo, telefono, tipo_sangre, centro_salud, fecha_fallecimiento_hora, fecha_hora_ablacion, lista_organos)
                            INCUCAI.registrar_paciente_donante(PACIENTE_DONANTE)
                            j += 1
                        else:
                            print('Debe ingresar "R" o "D"')
                break
        case 2:
            centro_salud = None
            while centro_salud == None:
                try:
                    centro_salud_num = int(input('Ingrese su centro de salud afiliado: (1. ALEMAN 2. SWISSMEDICAL 3. AUSTRAL 4. BRITANICO): '))
                    if centro_salud_num == 1 :
                        centro_salud = ALEMAN
                        INCUCAI.imprimir_lista_espera(centro_salud)
                    elif centro_salud_num == 2:
                        centro_salud = SWISSMEDICAL
                        INCUCAI.imprimir_lista_espera(centro_salud)
                    elif centro_salud_num == 3:
                        centro_salud = AUSTRAL 
                        INCUCAI.imprimir_lista_espera(centro_salud)
                    elif centro_salud_num == 4:
                        centro_salud = BRITANICO
                        INCUCAI.imprimir_lista_espera(centro_salud)
                    else: 
                        print('Por favor, ingrese un número válido.')
                        centro_salud = None
                except ValueError:
                    print('Por favor, ingrese un número válido.')
                    centro_salud = None
        case 3:
            resultado = 0
            while resultado != 1 :
                try:
                    dni = int(input("Ingrese el DNI del paciente receptor que quiere buscar"))
                    if dni > 0:
                        resultado = INCUCAI.prioridad_paciente(dni)
                except ValueError:
                    print('Debe ingresar un número valido.')
                    dni = 0
        case 4:
            INCUCAI.imprimir_donantes_receptores()
        case _:
            print("Opción no válida")
# Ejemplo de uso
while True:
    opcion = int(input("Elige una opción: \n1. Registrar paciente nuevo:\n2. Buscar por centro de salud los pacientes de la lista de espera\n3. Informar la prioridad de un paciente: \n4. Imprimir la lista pacientes donantes y receptores:\n"))
    menu(opcion)
    continuar = input("¿Querés volver al menú? (si/no): ").lower()
    if continuar != "si":
        print("Saliendo del sistema...")
        break