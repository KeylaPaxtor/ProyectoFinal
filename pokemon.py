# creación de la clase abstracta
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self._nombre = nombre
        self.__hp_actual = hp_maximo
        self.__hp_maximo = hp_maximo
        self.__energia_actual = energia_maxima
        self.__energia_maxima = energia_maxima

    # Encapsulamiento
    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, puntos_hp):
        if puntos_hp < 0:
            self.__hp_actual = 0
        else:
            self.__hp_actual = puntos_hp

    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, puntos_energia):
        if puntos_energia < 0:
            self.__energia_actual = 0
        else:
            self.__energia_actual = puntos_energia

    @abstractmethod
    def atacar(self, oponente):
        pass

    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            print(f'{self.nombre} se proteje')
        else:
            print('No tienes suficiente energía para defender.')

    def descansar(self):
        self.energia_actual += 20
        print(f'{self.nombre} recuperó energía.')