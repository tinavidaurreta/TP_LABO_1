class ErrDeCirujano(Exception):

    def __init__(self):
        super().__init__("No se encontro un cirujano disponible")
