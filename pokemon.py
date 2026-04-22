# creación de la clase abstracta
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self._nombre = nombre
        self._hp_actual = hp_maximo
        self._hp_maximo = hp_maximo
        self._energia_actual = energia_maxima
        self._energia_maxima = energia_maxima

# Encapsulamiento
    @property
    def hp_actual(self):
        return self._hp_actual

    @hp_actual.setter
    def hp_actual(self, puntos_hp):
        if puntos_hp < 0:
            self._hp_actual = 0
        else:
            self._hp_actual = puntos_hp

    @property
    def energia_actual(self):
        return self._energia_actual

    @energia_actual.setter
    def energia_actual(self, puntos_energia):
        if puntos_energia < 0:
            self._energia_actual = 0
        else:
            self._energia_actual = puntos_energia