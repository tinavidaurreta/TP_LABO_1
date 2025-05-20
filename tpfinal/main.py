from incucai import *


DRFELIPE = Generales()
DRAMARTINA = Especialista('cardiovascular')
DRALFREDO = Especialista('pulmonar')
DRSEBASTIAN = Especialista('traumatologo')
DRJOAQUIN = Generales()
DRAMERCEDES = Especialista('plastioco')
DRJAVIER = Especialista('gastroenterologo')
HELICOPTERO = Helicoptero(300, 0, 500, 0)#TRAFICO SE SUMA EN KM A LA DIST
AVION = Avion(800, 0, 1000, 0)
AUTO_1 = Auto(100, 0, 50, 30)
AUTO_2 = Auto(60, 0, 80, 30)
AUTO_3 = Auto(130, 0, 150, 50)
ALEMAN = CentrosSalud("Aleman", 'Av.Pueyrredon 1640', 'CABA', 'BuenasAires', 1148277000, [DRFELIPE, DRAMARTINA],[HELICOPTERO,AVION,AUTO_1, AUTO_2])
SWISSMEDICAL = CentrosSalud("SwissMedical", 'SanMartindeTours 2980', 'Capital', 'Cordoba', 8103338876 , [DRALFREDO, DRSEBASTIAN], [HELICOPTERO,AVION,AUTO_3])
AUSTRAL = CentrosSalud("Austral", 'Av.Pres.JuanDomingoPeron 1500', 'Pilar', 'BuenosAires', 2304482000 , [DRJAVIER, DRAMERCEDES,DRJOAQUIN], [HELICOPTERO,AVION,AUTO_3])
fecha_clara = datetime(2004, 5, 14)
fecha_juana = datetime(2004, 2, 13)
fecha_felipe = datetime(2004, 12, 18)
fecha_justo = datetime(2003, 5, 20)
CLARA = Donantes(46111111, 'Clara', fecha_clara, 'F', 1128112222, 'AB', ALEMAN, 0, 0, ['corazon', 'piel', 'higado','pancreas'])
JUANA = Receptores(46222222, 'Juana',fecha_juana, 'F', 1123459876, 'A', SWISSMEDICAL, 0 , 4, 'hepatitis', False, 'higado')# Inestable: False, Estable: True
FELIPE = Receptores(46222333, 'Felipe',fecha_felipe, 'M', 1145454545, 'AB' , AUSTRAL, 0, 2, 'FibrosisQuistica', True, 'pulmon')
JUSTO = Receptores(46333111, 'Justo', fecha_justo, 'M', 1145451111, 'B', SWISSMEDICAL, 0, 3, 'Paro', True, 'corazon')

receptores=[FELIPE, JUANA, JUSTO]
donantes = [CLARA]
cantidad = input('Ingrese cuanta cantidad de pacientes quiere registrar')
if cantidad > 0:
    for j in range(0,cantidad,1):
        x = input('Ingrese "R" si va a ingresar un paciente receptor o ingrese "D" si va a ingresar un paciente donante:' )
        if x == 'R' :
            DNI = input ('Ingrese su DNI:')
            nombre_apellido = input ('Ingrese su nombre y apellido:')
            fecha_str = input("Ingrese una fecha de nacimiento en formato DD/MM/AAAA: ")
            sexo = input ('Ingrese su F o M segun su sexo:')
            telefono = input ('Ingrese su numero de telefono:')
            tipo_sangre = input ('Ingrese su tipo de sangre (A / AB / B / 0):')
            for i in range(0,5,1):
                centro_salud_num = input ('Ingrese su centro de salud afiliado: (1. ALEMAN 2. SWISSMEDICAL 3.AUSTRAL)') 
                if centro_salud_num == 1 :
                    centro_salud = ALEMAN
                    break
                elif centro_salud_num == 2:
                    centro_salud = SWISSMEDICAL
                    break
                elif centro_salud_num == 3:
                    centro_salud = AUSTRAL 
                    break
                else :
                    ('No Ingreso un centro de salud dentro de las opciones')
            patologia = input ('Ingrese su patologia:')
            organo = input ('Ingrese el organo necesitante:')
            PACIENTE_RECEPTOR = Receptores(DNI, nombre_apellido, fecha_str, sexo, telefono, tipo_sangre, centro_salud, 0, patologia, True, organo ) # Siempre True hasta que se opere y cambie
            receptores.append(PACIENTE_RECEPTOR) 
        elif x == 'D':
            DNI = input ('Ingrese su DNI:')
            nombre_apellido = input ('Ingrese su nombre y apellido:')
            fecha_str = input("Ingrese una fecha de nacimiento en formato DD/MM/AAAA: ")
            sexo = input ('Ingrese su F o M segun su sexo:')
            telefono = input ('Ingrese su numero de telefono:')
            tipo_sangre = input ('Ingrese su tipo de sangre (A / AB / B / 0):')
            for i in range(0,5,1):
                centro_salud_num = input ('Ingrese su centro de salud afiliado: (1. ALEMAN 2. SWISSMEDICAL 3.AUSTRAL)')
                if centro_salud_num == 1 :
                    centro_salud = ALEMAN
                    break
                elif centro_salud_num == 2:
                    centro_salud = SWISSMEDICAL
                    break
                elif centro_salud_num == 3:
                    centro_salud = AUSTRAL 
                    break
                else :
                    ('No Ingreso un centro de salud dentro de las opciones')
            organos = input ('Ingrese el los organos donantes:')
            palabra = ""
            lista_organos = []
            for caracter in organos:
                if caracter != " ":
                    palabra += caracter  # va construyendo la palabra
                elif palabra:
                        lista_organos.append(palabra)
                        palabra = ""  # reinicia para la siguiente palabra
            # Añadir la última palabra si no termina con espacio
            if palabra:
                lista_organos.append(palabra)
            PACIENTE_DONANTE = Donantes(DNI, nombre_apellido, fecha_str, sexo, telefono, tipo_sangre, centro_salud, 0, 0, lista_organos)
            donantes.append(PACIENTE_DONANTE)

    INCUCAI= Incucai(receptores,donantes,[SWISSMEDICAL,AUSTRAL,ALEMAN])
    # Faltan excepciones y chequear que agregue bien, hacer mas medicos, mas sedes