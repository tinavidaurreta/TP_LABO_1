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
JUANA = Receptores(46222222, 'Juana',fecha_juana, 'F', 1123459876, 'AB', SWISSMEDICAL, 0 , 4, 'hepatitis', False, 'higado')# Inestable: False, Estable: True
FELIPE = Receptores(46222333, 'Felipe',fecha_felipe, 'M', 1145454545, 'AB' , AUSTRAL, 0, 2, 'FibrosisQuistica', True, 'pulmon')
JUSTO = Receptores(46333111, 'Justo', fecha_justo, 'M', 1145451111, 'B', SWISSMEDICAL, 0, 3, 'Paro', True, 'corazon')
INCUCAI=Incucai([],[CLARA],[SWISSMEDICAL,AUSTRAL,ALEMAN])

INCUCAI.registrar_paciente_receptor(FELIPE)
print(CLARA.listado_organos_donar)
print(INCUCAI.lista_receptores)

INCUCAI.registrar_paciente_receptor(JUANA)
print(CLARA.listado_organos_donar)
print(INCUCAI.lista_receptores)