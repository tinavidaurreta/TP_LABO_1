from incucai import *
from excepciones.expecion_char import ErrDeChar
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
AUTO_1 = Auto(100, 0, 50, 12000000000)
AUTO_2 = Auto(60, 0, 80, 1234565432)
AUTO_3 = Auto(130, 0, 150, 123456543)
ALEMAN = CentrosSalud("Aleman", 'Av.Pueyrredon 1640', 'CABA', 'BuenosAires', 1148277000, [DRFELIPE, DRAMARTINA],[HELICOPTERO,AVION,AUTO_1, AUTO_2, AUTO_3])
SWISSMEDICAL = CentrosSalud("SwissMedical", 'SanMartindeTours 2980', 'Capital', 'Cordoba', 8103338876 , [DRALFREDO, DRSEBASTIAN], [HELICOPTERO,AVION,AUTO_3])
BRITANICO = CentrosSalud("Britanico", "Solis 2171",'CABA','BuenosAires', 1143096400, [DRJAVIER],[AUTO_1,AUTO_2,AUTO_3])
AUSTRAL = CentrosSalud("Austral", 'Av.Pres.JuanDomingoPeron 1500', 'Pilar', 'BuenosAires', 2304482000 , [DRAMERCEDES,DRJOAQUIN], [HELICOPTERO,AVION,AUTO_3])
fecha_clara = datetime(2004, 5, 14)
fecha_juana = datetime(2004, 2, 13)
fecha_felipe = datetime(2004, 12, 18)
fecha_justo = datetime(2003, 5, 20)
CLARA = Donantes(46111111, 'Clara Gomez', fecha_clara, 'F', 1128112222, 'AB', ALEMAN, 0, 0, ['corazon', 'piel', 'higado','pancreas'])
JUANA = Receptores(46222222, 'Juana Kallis',fecha_juana, 'F', 1123459876, 'A', SWISSMEDICAL, 0 , 4, 'hepatitis', False, 'higado')# Inestable: False, Estable: True
FELIPE = Receptores(46222333, 'Felipe Nini',fecha_felipe, 'M', 1145454545, 'AB' , AUSTRAL, 0, 2, 'FibrosisQuistica', True, 'pulmon')
JUSTO = Receptores(46333111, 'Justo Larguia', fecha_justo, 'M', 1145451111, 'B', ALEMAN, 0, 3, 'Paro', True, 'corazon')
receptores=[FELIPE, JUANA, JUSTO]
donantes = [CLARA]
INCUCAI= Incucai(receptores,donantes,[SWISSMEDICAL,AUSTRAL,ALEMAN,BRITANICO])
cantidad = int(input('Ingrese cuanta cantidad de pacientes quiere registrar'))
#En caso de que se ingrese en formato texto
try:
    cantidad = int(cantidad)
except ValueError:
    print("Debe ingresar un número entero para la cantidad.")
    cantidad = 0

if cantidad > 0:
    for j in range(0,cantidad,1):
        x = input('Ingrese "R" si va a ingresar un paciente receptor o ingrese "D" si va a ingresar un paciente donante:' ).upper()
        try:
            if x != "R" or x != "D":
                raise ErrDeChar()
        except ErrDeChar as e:
            print(e)
            x = None
        if x == 'R' :
            DNI = input ('Ingrese su DNI:')
            nombre_apellido = input ('Ingrese su nombre y apellido:')
            fecha_str = input("Ingrese una fecha de nacimiento en formato DD/MM/AAAA: ")
            sexo = input ('Ingrese su F o M segun su sexo:')
            telefono = input ('Ingrese su numero de telefono:')
            tipo_sangre = input ('Ingrese su tipo de sangre (A / AB / B / 0):').upper()
            prioridad = random.randint(1,5)
            centro_salud = None
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
            except ValueError:
                print('Por favor, ingrese un número válido.')
            if centro_salud is None:
                print('No se pudo asignar un centro de salud válido, se asignará ALEMAN por defecto.')
                centro_salud = ALEMAN
            patologia = input ('Ingrese su patologia:')
            organo = input ('Ingrese el organo necesitante:').lower()
            fecha_lista_espera = datetime.now()
            PACIENTE_RECEPTOR = Receptores(DNI, nombre_apellido, fecha_str, sexo, telefono, tipo_sangre, centro_salud, fecha_lista_espera, prioridad, patologia, True, organo) # Siempre True hasta que se opere y cambie
            INCUCAI.registrar_paciente_receptor(PACIENTE_RECEPTOR)
            
        elif x == 'D':
            DNI = input ('Ingrese su DNI:')
            nombre_apellido = input ('Ingrese su nombre y apellido:')
            fecha_str = input("Ingrese una fecha de nacimiento en formato DD/MM/AAAA: ")
            sexo = input ('Ingrese su F o M segun su sexo:')
            telefono = input ('Ingrese su numero de telefono:')
            tipo_sangre = input ('Ingrese su tipo de sangre (A / AB / B / 0):').upper()
            centro_salud = None
            fecha_fallecimiento_hora = datetime.now()
            fecha_hora_ablacion = None
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
            except ValueError:
                print('Por favor, ingrese un número válido.')

            if centro_salud is None:
                print('No se pudo asignar un centro de salud válido, se asignará ALEMAN por defecto.')
                centro_salud = ALEMAN 
            organos = input ('Ingrese el/los organos donantes:').lower()
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
            INCUCAI.registrar_paciente_donante(PACIENTE_DONANTE)

    # Faltan excepciones y chequear que agregue bien, hacer mas medicos, mas sedes


"""try:
    #intentar acceder a un atributo exclusivo de receptor
    organo_requerido = receptores.organo

    centro_donante = donantes.centro_salud
    centro_receptor = receptores.centro_salud

    #asignar cirujano del centro de salud del donante
    cirujano = centro_donante.asignar_cirujano()
    if cirujano is None:
        print("No se pudo asignar un cirujano para el trasplante.")
    else:
        # asignar vehículo para transportar el órgano
        vehiculo = centro_donante.asignar_vehiculo(centro_receptor)
        print(f"Vehículo asignado: {type(vehiculo).__name__}")
        print(f"El medico asignado: {type(cirujano).__name__}")

        # realizar el trasplante
        exito = centro_donante.realizar_transplante(donantes.fecha_hora_ablacion, vehiculo, cirujano, organo_requerido)

        if exito:
            print("Trasplante exitoso.")
            
        else:
            print("El trasplante falló.")

except AttributeError:
    print("El paciente no es receptor, no se puede realizar el trasplante.")
"""