# creación de la clase abstracta
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self._nombre = nombre
        self._hp_actual = hp_maximo
        self._hp_maximo = hp_maximo
        self._energia_actual = energia_maxima
        self._energia_maxima = energia_maxima