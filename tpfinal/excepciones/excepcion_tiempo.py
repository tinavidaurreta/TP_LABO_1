import datetime



class ErrorDeTransplante(Exception):

    def __init__(self, tiempo_transcurrido:datetime):
        self.tiempo_transcurrido = tiempo_transcurrido
        super().__init__(f"Transcurrieron {tiempo_transcurrido}s que son mas de 20hrs de la fecha de ablacion")
