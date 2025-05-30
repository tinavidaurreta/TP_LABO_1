from incucai import *
import random 

DRFELIPE = Generales('Dr.Felipe Gonzles')
DRAMARTINA = Especialista('Dra.Martina Steiselboin','cardiovascular')
DRALFREDO = Especialista('Dr.Alfredo Vidaurreta','pulmonar')
DRSEBASTIAN = Especialista('Dr.Sebastian Vidaurreta','traumatologo')
DRJOAQUIN = Generales('Dr.Joaquin Villa')
DRAMERCEDES = Especialista('Dra.Mercedes Galardi','plastico')
DRJAVIER = Especialista('Dr.Javier Martinez','gastroenterologo')
DRLAURA = Especialista('Dra.Laura Fernández', 'cardiovascular')
DRMARIO = Generales('Dr.Mario Gutiérrez')
DRVALERIA = Especialista('Dra.Valeria Pineda', 'pulmonar')
DRCARLOS = Generales('Dr.Carlos Medina')
HELICOPTERO = Helicoptero(300, 0, 500, 0)#TRAFICO SE SUMA EN KM A LA DIST
AVION = Avion(800, 0, 1000, 0)
AUTO_1 = Auto(100, 0, 50, 0)
AUTO_2 = Auto(60, 0, 80, 900000000000)
AUTO_3 = Auto(130, 0, 150, 0)
ALEMAN = CentrosSalud('Aleman', 'Av.Pueyrredon 1640', 'CABA', 'BuenosAires', 1148277000, [DRFELIPE, DRAMARTINA,DRLAURA],[HELICOPTERO,AVION,AUTO_1, AUTO_2, AUTO_3])
SWISSMEDICAL = CentrosSalud('SwissMedical', 'SanMartindeTours 2980', 'Capital', 'Cordoba', 8103338876 , [DRALFREDO,DRMARIO], [HELICOPTERO,AVION,AUTO_1])
BRITANICO = CentrosSalud('Britanico', 'Solis 2171','CABA','BuenosAires', 1143096400, [DRJAVIER, DRSEBASTIAN,DRVALERIA],[AUTO_1,AUTO_2,AVION,HELICOPTERO])
AUSTRAL = CentrosSalud('Austral', 'Av.Pres.JuanDomingoPeron 1500', 'Pilar', 'BuenosAires', 2304482000 , [DRAMERCEDES,DRJOAQUIN,DRCARLOS], [HELICOPTERO,AVION,AUTO_2])
fecha_clara = datetime(2004, 5, 14)
fecha_simon = datetime(2004, 2, 13)
fecha_felipe = datetime(2004, 12, 18)
fecha_justo = datetime(2003, 5, 20)
fecha_maria = datetime(2005, 6, 20)
CLARA = Donantes(46111111, 'Clara Gomez', fecha_clara, 'F', 1128112222, 'AB', ALEMAN, 0, 0, ['corazon', 'piel', 'higado','pancreas'])
SIMON = Receptores(46222222, 'Simon Villanueva',fecha_simon, 'M', 1123459876, 'A', SWISSMEDICAL, 0 , 4, 'hepatitis', False, 'higado')# Inestable: False, Estable: True
FELIPE = Receptores(46333333, 'Felipe Nini',fecha_felipe, 'M', 1145454545, 'A' , AUSTRAL, 0, 2, 'FibrosisQuistica', True, 'pulmon')
JUSTO = Receptores(46444444, 'Justo Larguia', fecha_justo, 'M', 1145451111, 'B', ALEMAN, 0, 3, 'Paro', True, 'corazon')
MARIA = Receptores(46555555, 'Maria Gonzal', fecha_maria, 'M', 1145452222, 'A', ALEMAN, 0, 3, 'Paro', True, 'corazon')
receptores=[FELIPE, SIMON, JUSTO, MARIA]
donantes = [CLARA]
INCUCAI= Incucai(receptores,donantes,[SWISSMEDICAL,AUSTRAL,ALEMAN,BRITANICO])

def menu(opcion):
    match opcion:
        case 1:
            cantidad = 0
            while cantidad == 0:
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
                            dni_str = (input ('Ingrese su DNI (8 cifras): ')) 
                            while not (dni_str.isdigit() and len(dni_str) == 8):
                                print('DNI no valido. Debe ingresar un dni de 8 cifras')
                                dni_str= input('Ingrese su DNI (8 cifras): ')
                            DNI = int(dni_str)
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
                            dni_str = (input ('Ingrese su DNI (8 cifras): ')) #ELEMENTAL
                            while not (dni_str.isdigit() and len(dni_str) == 8):
                                print('DNI no valido. Debe ingresar un dni de 8 cifras')
                                dni_str= input('Ingrese su DNI (8 cifras): ')
                            DNI = int(dni_str)
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
                            lista_organos =[]
                            while True:
                                organo = input ('Ingrese el/los organos donantes (con espacio entre medio):').lower()
                                lista_organos.append(organo)
                                respuesta = input("¿Querés agregar otro órgano? (si/no): ").lower()
                                if respuesta != "si":
                                    break
                            PACIENTE_DONANTE = Donantes(DNI, nombre_apellido, fecha_str, sexo, telefono, tipo_sangre, centro_salud, fecha_fallecimiento_hora, fecha_hora_ablacion, lista_organos)
                            INCUCAI.registrar_paciente_donante(PACIENTE_DONANTE)
                            j += 1
                        else:
                            print('Debe ingresar "R" o "D"')
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
            while resultado != 1:
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
    try:
        opcion = int(input("Elige una opción: \n1. Registrar paciente nuevo:\n2. Buscar por centro de salud los pacientes de la lista de espera\n3. Informar la prioridad de un paciente: \n4. Imprimir la lista pacientes donantes y receptores:\n"))
    except ValueError:
        print('Por favor, ingrese un número válido.')
    else:
        menu(opcion)
    finally:
        while True:
            continuar = input("¿Querés volver al menú? (si/no): ").lower()
            if continuar == "si":
                break
            elif continuar == "no":
                print("Saliendo del sistema...")
                exit()
            else:
                print('opcion no valida. Solo se permite "si" o "no"')
            