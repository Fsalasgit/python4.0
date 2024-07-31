from math import pi

class Tanque:
    def __init__(self, diametro=1.0, altura=1.0):
        self.diametro = diametro
        self.altura = altura
        self.valvulas = []
        self.nivelActual = 0
        self.caudal = 0
        self.volumenActual = 0

    def calcularNivel(self):
        pass

    def update(self, tiempo = 1):
        pass

    def cargarTanque(self):
        pass

    def vaciarTanque(self):
        pass

class Valvula:
    def __init__(self, tipo="E", caudal=1.0):
        self.tipo = tipo
        self.caudal = caudal
        self.caudalActual = 0

    def abrirValvula(self):
        pass

    def cerrarValvula(self):
        pass

