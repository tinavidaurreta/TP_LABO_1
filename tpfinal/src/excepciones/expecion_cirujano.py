class ErrDeCirujano(Exception):
    """ 
    Esta clase crea un error personalizado por si no se encontro un cirujano
    """

    def __init__(self):
        super().__init__("No se encontro un cirujano disponible")
